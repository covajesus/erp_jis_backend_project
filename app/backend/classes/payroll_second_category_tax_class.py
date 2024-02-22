from app.backend.db.models import PayrollSecondCategoryTaxModel
from datetime import datetime

class PayrollSecondCategoryTaxClass:
    def __init__(self, db):
        self.db = db
          
    def get(self, rut, taxable_id):
        data = self.db.query(PayrollSecondLevelModel).filter(PayrollItemValueModel.rut == rut, PayrollItemValueModel.item_id == taxable_id).first()

        return data
    

    def store(self, payroll_indicator_inputs):
        try:
            payroll_taxable_income_cap_indicator = PayrollTaxableIncomeCapIndicatorModel()
            payroll_taxable_income_cap_indicator.afp = cap_income_tax_afp
            payroll_taxable_income_cap_indicator.ips = cap_income_tax_ips
            payroll_taxable_income_cap_indicator.unemployment = cap_income_tax_unemployment
            payroll_taxable_income_cap_indicator.added_date = datetime.now()
            payroll_taxable_income_cap_indicator.updated_date = datetime.now()
            self.db.add(payroll_taxable_income_cap_indicator)
            self.db.commit()
            
            inserted_id = payroll_taxable_income_cap_indicator.id

            return inserted_id
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"