from app.backend.db.models import PayrollTaxableIncomeCapIndicatorModel
from app.backend.classes.helper_class import HelperClass
from datetime import datetime

class PayrollTaxableIncomeCapIndicatorClass:
    def __init__(self, db):
        self.db = db
    
    def store(self, payroll_indicator_inputs):
        try:
            cap_income_tax_afp = HelperClass().remove_from_string(".", payroll_indicator_inputs['cap_income_tax_afp'])
            cap_income_tax_afp = HelperClass().replace(",", ".", cap_income_tax_afp)
            cap_income_tax_ips = HelperClass().remove_from_string(".", payroll_indicator_inputs['cap_income_tax_ips'])
            cap_income_tax_ips = HelperClass().replace(",", ".", cap_income_tax_ips)
            cap_income_tax_unemployment = HelperClass().remove_from_string(".", payroll_indicator_inputs['cap_income_tax_unemployment'])
            cap_income_tax_unemployment = HelperClass().replace(",", ".", cap_income_tax_unemployment)

            payroll_taxable_income_cap_indicator = PayrollTaxableIncomeCapIndicatorModel()
            payroll_taxable_income_cap_indicator.afp = cap_income_tax_afp
            payroll_taxable_income_cap_indicator.ips = cap_income_tax_ips
            payroll_taxable_income_cap_indicator.unemployment = cap_income_tax_unemployment
            payroll_taxable_income_cap_indicator.added_date = datetime.now()
            self.db.add(payroll_taxable_income_cap_indicator)
            self.db.commit()
            
            inserted_id = payroll_taxable_income_cap_indicator.id

            return inserted_id
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"