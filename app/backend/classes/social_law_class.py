from app.backend.db.models import EmployeeModel, HealthModel, EmployeeExtraModel, NationalityModel, RegimeModel, EmployeeLaborDatumModel, PayrollEmployeeModel, SocialLawModel, GenderModel
from app.backend.classes.payroll_item_value_class import PayrollItemValueClass
from app.backend.classes.helper_class import HelperClass
from app.backend.classes.payroll_period_class import PayrollPeriodClass
from datetime import datetime
from app.backend.classes.medical_license_class import MedicalLicenseClass

class SocialLawClass:
    def __init__(self, db):
        self.db = db

    def store(self, period):
        try:
            social_laws = self.db.query(SocialLawModel).filter(SocialLawModel.period == period).all()
                
            for social_law in social_laws:
                employee_labor_data = self.db.query(EmployeeLaborDatumModel).filter(EmployeeLaborDatumModel.rut == social_law.rut).first()
                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 70, period)
                disability_insurance_quote = payroll_item_value.amount

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 4, period)
                pention_voluntary_savings = payroll_item_value.amount

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 41, period)
                health = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 29, period)
                extra_health = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 24, period)
                ccaf_personal_credit = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 71, period)
                ccaf_secure_life = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 72, period)
                ccaf_leasing_discount = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 73, period)
                ccaf_no_isapre_affiliate_quote = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 10, period)
                ccaf_family_discount_members = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 74, period)
                mutuality_value = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 30, period)
                worker_unemployment_insurance = payroll_item_value

                payroll_item_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 61, period)
                employer_unemployment_insurance = payroll_item_value

                health_data = self.db.query(HealthModel).filter(HealthModel.id == employee_labor_data.health_id).first()

                taxable_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 38, period)
                pention_value = PayrollItemValueClass(self.db).get_with_period(social_law.rut, 59, period)
                social_law_employee = self.db.query(SocialLawModel).filter(SocialLawModel.rut == social_law.rut).first()
                social_law_employee.pention_taxable_income = taxable_value.value
                social_law_employee.pention_mandatory_contribution = pention_value.value
                social_law_employee.disability_insurance_quote = disability_insurance_quote.value
                social_law_employee.pention_voluntary_savings = pention_voluntary_savings.value
                social_law_employee.apvi_number_contract = 1
                social_law_employee.apvi_payment_type = 1
                social_law_employee.apvc_payment_type = 1
                social_law_employee.voluntary_affiliate_movement_code = social_law.movement_code
                social_law_employee.voluntary_affiliate_since_date = social_law.period_since
                social_law_employee.voluntary_affiliate_since_date = social_law.period_until
                social_law_employee.number_quote_periods = 1
                social_law_employee.ips_isl_fonasa_taxable_value = social_law.taxable_value

                if employee_labor_data.regime_id == 1:
                    social_law_employee.ex_cashier_regime_code = 

                if employee_labor_data.health_id == 2:
                    social_law_employee.fonasa_health_quote = health.value
                    social_law_employee.health_institution_code = health_data.social_law
                    social_law_employee.plan_payment_type = 1
                else:
                    social_law_employee.isapre_taxable_value = 0
                    social_law_employee.health_institution_code = health_data.social_law
                    social_law_employee.plan_payment_type = 2
                    social_law_employee.isapre_quote = employee_labor_data.extra_health_amount
                    social_law_employee.isapre_mandatory_quote = health.amount
                    social_law_employee.isapre_aditional_quote = extra_health.amount

                social_law_employee.ccaf_code = 1
                social_law_employee.ccaf_taxable_value = social_law.taxable_value
                social_law_employee.ccaf_personal_credit = ccaf_personal_credit.amount
                social_law_employee.ccaf_secure_life = ccaf_secure_life.amount
                social_law_employee.ccaf_leasing_discount = ccaf_leasing_discount.amount
                social_law_employee.ccaf_no_isapre_affiliate_quote = ccaf_no_isapre_affiliate_quote.amount
                social_law_employee.ccaf_family_discount_members = ccaf_family_discount_members.amount
                social_law_employee.mutuality_code = 1
                social_law_employee.mutuality_taxable_code = social_law.taxable_value
                social_law_employee.mutuality_work_accident = mutuality_value.amount
                social_law_employee.unemployment_insurance_taxable_value = social_law.taxable_value
                social_law_employee.unemployment_insurance_employee_quote = worker_unemployment_insurance.amount
                social_law_employee.unemployment_insurance_employeer_quote = employer_unemployment_insurance.amount

                if social_law.movement_code == 3:
                    social_law_employee.subsidy_payer_rut = health_data.rut
                    social_law_employee.subsidy_payer_dv = health_data.dv

                self.db.add(social_laws)
                self.db.commit()

            return social_law_employee.id
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
   