from app.backend.classes.payroll_employee_class import PayrollEmployeeClass
from app.backend.classes.payroll_item_value_class import PayrollItemValueClass
from app.backend.classes.payroll_taxable_income_cap_indicator_class import PayrollTaxableIncomeCapIndicatorClass
from app.backend.classes.payroll_item_class import PayrollItemClass
from app.backend.classes.payroll_uf_indicator_class import PayrollUfIndicatorClass
from app.backend.classes.payroll_minium_taxable_income_indicator_class import PayrollMiniumTaxableIncomeIndicatorClass
from app.backend.classes.payroll_afp_quote_indicator_class import PayrollAfpQuoteIndicatorClass
from app.backend.classes.payroll_umployment_insurance_indicator_class import PayrollUmploymentInsuranceIndicatorClass
from app.backend.classes.payroll_second_category_tax_class import PayrollSecondCategoryTaxClass

class PayrollCalculationClass:
    def __init__(self, db):
        self.db = db

    # Función para calcular la planilla de sueldos
    def calculate(self, period = None):
        employees = PayrollEmployeeClass(self.db).get_all(period)

        for employee in employees:
            # 1
            self.proportional(employee['rut'], 35, period, 0, 1)
            # 2
            self.proportional(employee['rut'], 36, period, 0, 1)
            # 3
            self.proportional(employee['rut'], 37, period, 0, 1)
            # 4
            taxable_salary = self.taxable_salary(employee['rut'], period)
            # 5
            no_taxable_salary = self.no_taxable_salary(employee['rut'], period)
            # 6
            gratification = self.gratification(employee['rut'], period, taxable_salary)
            # 7
            taxable_assets = self.taxable_assets(employee['rut'], period, taxable_salary, gratification)
            # 8
            self.no_taxable_assets(employee['rut'], period, no_taxable_salary)

            #//////////////////////////////////////////////////////////////////////////////////////////

            # 9
            self.health(employee['rut'], period, employee['extra_health_payment_type_id'], employee['extra_health_amount'], taxable_assets)

            # 10
            self.pention(employee['rut'], period, employee['pention_id'], taxable_assets)

            # 11
            self.worker_unemployment_insurance(employee['rut'], period, employee['regime_id'], employee['contract_type_id'], taxable_assets)

            # 12
            self.employer_unemployment_insurance(employee['rut'], period, employee['regime_id'], employee['contract_type_id'], taxable_assets)

            # 13
            self.legal_discount(employee['rut'], period)

            # 14
            self.other_discount(employee['rut'], period)

            # self.second_level_insurance(employee['rut'], period, taxable_assets)

    def taxable_salary(self, rut, period):
        taxable_items = PayrollItemClass(self.db).get_no_taxable_items()

        taxable_total = 0

        for taxable_item in taxable_items:
            payroll_item_value = PayrollItemValueClass(self.db).get(rut, taxable_item.id)

            if payroll_item_value.classification_id == 1:
                taxable_total += payroll_item_value.amount
            elif  payroll_item_value.classification_id == 2:
                taxable_total -= payroll_item_value.amount

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 38
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = taxable_total

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return taxable_total
    
    def proportional(self, rut, item_id, period, amount = 0, manual_status_id = 0):
        if manual_status_id == 1:
            payroll_item_value = PayrollItemValueClass(self.db).get_with_period(rut, item_id, period)
            days = PayrollItemValueClass(self.db).get_with_period(rut, 55, period)

            total = (payroll_item_value.amount / 30) * days.amount

            if item_id == 35:
                item_id = 52
            elif item_id == 36:
                item_id = 53
            elif item_id == 37:
                item_id = 54

            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = item_id
            payroll_item_value_data['rut'] = rut
            payroll_item_value_data['period'] = period
            payroll_item_value_data['amount'] = total

            PayrollItemValueClass(self.db).store(payroll_item_value_data)
        else:
            days = PayrollItemValueClass(self.db).get_with_period(rut, 55, period)

            total = (amount / 30) * days.amount
    
    def no_taxable_salary(self, rut, period):
        taxable_items = PayrollItemClass(self.db).get_taxable_items()

        no_taxable_total = 0

        for taxable_item in taxable_items:
            payroll_item_value = PayrollItemValueClass(self.db).get(rut, taxable_item.id)

            no_taxable_total += payroll_item_value.amount

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 40
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = no_taxable_total

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return no_taxable_total
    
    def gratification(self, rut, period, imponible_salary):
        payroll_minium_taxable_income_indicator = PayrollMiniumTaxableIncomeIndicatorClass(self.db).get(period)
        top_minimal_salary = payroll_minium_taxable_income_indicator.dependent_independent_workers
        cap_value = (top_minimal_salary * 4.75)/12

        if (imponible_salary * 0.25) > cap_value:
            amount = cap_value
        else:
            amount = imponible_salary * 0.25

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 40
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return amount
    
    def taxable_assets(self, rut, period, taxable_salary, gratification):
        amount = taxable_salary + gratification

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 57
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return amount

    def no_taxable_assets(self, rut, period, no_taxable_salary):
        amount = no_taxable_salary

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 58
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

    def health(self, rut, period, extra_health_payment_type_id, extra_health_amount, taxable_assets):
        payroll_taxable_income_cap_indicator = PayrollTaxableIncomeCapIndicatorClass(self.db).get(period)
        payroll_uf_indicator = PayrollUfIndicatorClass(self.db).get(period)

        if extra_health_payment_type_id > 0:
            if extra_health_payment_type_id == 1:
                extra_amount = extra_health_amount

                health_amount = self.proportional(rut, period, 0, extra_amount, 0)

                if taxable_assets > payroll_taxable_income_cap_indicator.afp:
                    aditional_health_amount = health_amount - (payroll_taxable_income_cap_indicator.afp * 0.07);
                else:
                    aditional_health_amount = health_amount - (taxable_assets * 0.07);
            else:
                extra_uf_amount = extra_health_amount * payroll_uf_indicator.uf_value_current_month

                health_amount = self.proportional(rut, period, 0, extra_uf_amount, 0)

                if taxable_assets > payroll_taxable_income_cap_indicator.afp:
                    aditional_health_amount = health_amount - (payroll_taxable_income_cap_indicator.afp * 0.07);
                else:
                    aditional_health_amount = health_amount - (taxable_assets * 0.07);
        
            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = 41
            payroll_item_value_data['rut'] = rut
            payroll_item_value_data['period'] = period
            payroll_item_value_data['amount'] = health_amount

            PayrollItemValueClass(self.db).store(payroll_item_value_data)

            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = 29
            payroll_item_value_data['rut'] = rut
            payroll_item_value_data['period'] = period
            payroll_item_value_data['amount'] = aditional_health_amount

            PayrollItemValueClass(self.db).store(payroll_item_value_data)
        else:
            if taxable_assets > payroll_taxable_income_cap_indicator.afp:
                amount = payroll_taxable_income_cap_indicator.afp * 0.07
            else:
                amount = taxable_assets * 0.07

            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = 41
            payroll_item_value_data['rut'] = rut
            payroll_item_value_data['period'] = period
            payroll_item_value_data['amount'] = amount

            PayrollItemValueClass(self.db).store(payroll_item_value_data)

    def pention(self, rut, period, pention_id, taxable_assets):
        payroll_taxable_income_cap_indicator = PayrollTaxableIncomeCapIndicatorClass(self.db).get(period)
        payroll_afp_quote = PayrollAfpQuoteIndicatorClass(self.db).get(pention_id, period)

        if taxable_assets > payroll_taxable_income_cap_indicator.afp:
            pention_amount = payroll_afp_quote.dependent_rate_afp * payroll_afp_quote.dependent_rate_afp
        else:
            pention_amount = taxable_assets * payroll_afp_quote.dependent_rate_afp

        amount = self.proportional(rut, 0, period, pention_amount, 0)

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 59
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

    def worker_unemployment_insurance(self, rut, period, regime_id, contract_type_id, taxable_assets):
        payroll_taxable_income_cap_indicator = PayrollTaxableIncomeCapIndicatorClass(self.db).get(period)

        if regime_id == 2 or regime_id == 3:
            amount = 0
        else:
            payroll_item_value_days = PayrollItemValueClass(self.db).get_with_period(rut, period, 55)

            payroll_umployment_insurance_indicator = PayrollUmploymentInsuranceIndicatorClass(self.db).get(contract_type_id, period)

            if payroll_item_value_days.amount > 0:
                if taxable_assets > payroll_taxable_income_cap_indicator.afp:
                    taxable_assets = payroll_taxable_income_cap_indicator.afp

                if contract_type_id == 1:
                    amount = (payroll_umployment_insurance_indicator.worker/100) * taxable_assets
                elif contract_type_id == 2:
                    amount = (payroll_umployment_insurance_indicator.worker/100) * taxable_assets
                else:
                    amount = (payroll_umployment_insurance_indicator.worker/100) * taxable_assets
            else:
                payroll_item_value_taxable_assets = PayrollItemValueClass(self.db).get(rut, 60)

                if payroll_item_value_taxable_assets.amount > payroll_taxable_income_cap_indicator.afp:
                    taxable_assets = payroll_taxable_income_cap_indicator.afp
                else:
                    taxable_assets = payroll_item_value_taxable_assets.amount

                if contract_type_id == 1:
                    amount = (payroll_umployment_insurance_indicator.worker/100) * taxable_assets
                elif contract_type_id == 2:
                    amount = (payroll_umployment_insurance_indicator.worker/100) * taxable_assets
                else:
                    amount = (payroll_umployment_insurance_indicator.worker/100) * taxable_assets

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 30
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

    def employer_unemployment_insurance(self, rut, period, regime_id, contract_type_id, taxable_assets):
        payroll_taxable_income_cap_indicator = PayrollTaxableIncomeCapIndicatorClass(self.db).get(period)

        if regime_id == 2 or regime_id == 3:
            amount = 0
        else:
            payroll_item_value_days = PayrollItemValueClass(self.db).get_with_period(rut, period, 55)

            payroll_umployment_insurance_indicator = PayrollUmploymentInsuranceIndicatorClass(self.db).get(contract_type_id, period)

            if payroll_item_value_days.amount > 0:
                if taxable_assets > payroll_taxable_income_cap_indicator.afp:
                    taxable_assets = payroll_taxable_income_cap_indicator.afp

                if contract_type_id == 1:
                    amount = (payroll_umployment_insurance_indicator.employer/100) * taxable_assets
                elif contract_type_id == 2:
                    amount = (payroll_umployment_insurance_indicator.employer/100) * taxable_assets
                else:
                    amount = (payroll_umployment_insurance_indicator.employer/100) * taxable_assets
            else:
                payroll_item_value_taxable_assets = PayrollItemValueClass(self.db).get(rut, 60)

                if payroll_item_value_taxable_assets.amount > payroll_taxable_income_cap_indicator.afp:
                    taxable_assets = payroll_taxable_income_cap_indicator.afp
                else:
                    taxable_assets = payroll_item_value_taxable_assets.amount

                if contract_type_id == 1:
                    amount = (payroll_umployment_insurance_indicator.employer/100) * taxable_assets
                elif contract_type_id == 2:
                    amount = (payroll_umployment_insurance_indicator.employer/100) * taxable_assets
                else:
                    amount = (payroll_umployment_insurance_indicator.employer/100) * taxable_assets

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 61
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

    def legal_discount(self, rut, period):
        legal_discount_items = PayrollItemClass(self.db).get_()

        legal_discount_total = 0

        for legal_discount_item in legal_discount_items:
            legal_discount_item_value = PayrollItemValueClass(self.db).get(rut, legal_discount_item.id)

            legal_discount_total += legal_discount_item_value.amount

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 63
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = legal_discount_total

        PayrollItemValueClass(self.db).store(payroll_item_value_data)


    def other_discount(self, rut, period):
        other_discount_items = PayrollItemClass(self.db).get_()

        other_discount_total = 0

        for other_discount_item in other_discount_items:
            other_discount_item_value = PayrollItemValueClass(self.db).get(rut, other_discount_item.id)

            other_discount_total += other_discount_item_value.amount

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 64
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = other_discount_total

        PayrollItemValueClass(self.db).store(payroll_item_value_data)

    def second_level_insurance(self, rut, period, taxable_assets):
        payroll_second_category_tax_indicator = PayrollSecondCategoryTaxClass(self.db).get(period, taxable_assets)

        amount = payroll_second_category_tax_indicator.discount

        payroll_item_value_data = {}
        payroll_item_value_data['item_id'] = 65
        payroll_item_value_data['rut'] = rut
        payroll_item_value_data['period'] = period
        payroll_item_value_data['amount'] = amount

        PayrollItemValueClass(self.db).store(payroll_item_value_data)