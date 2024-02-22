from app.backend.db.models import PayrollSecondCategoryTaxModel
from datetime import datetime

class PayrollSecondCategoryTaxClass:
    def __init__(self, db):
        self.db = db
          
    def get(self, period):
        data = self.db.query(PayrollSecondCategoryTaxModel).filter(PayrollSecondCategoryTaxModel.period == period).first()

        return data
    

    def store(self, payroll_sencond_category_tax_inputs):
        try:
            payroll_second_category_tax = PayrollSecondCategoryTaxModel()
            payroll_second_category_tax.period = payroll_sencond_category_tax_inputs['period']
            payroll_second_category_tax.since = payroll_sencond_category_tax_inputs['since_1']
            payroll_second_category_tax.until = payroll_sencond_category_tax_inputs['until_1']
            payroll_second_category_tax.factor = payroll_sencond_category_tax_inputs['factor_1']
            payroll_second_category_tax.discount = payroll_sencond_category_tax_inputs['discount_1']
            payroll_second_category_tax.added_date = datetime.now()
            payroll_second_category_tax.updated_date = datetime.now()
            self.db.add(payroll_second_category_tax)
            self.db.commit()

            payroll_second_category_tax = PayrollSecondCategoryTaxModel()
            payroll_second_category_tax.period = payroll_sencond_category_tax_inputs['period']
            payroll_second_category_tax.since = payroll_sencond_category_tax_inputs['since_2']
            payroll_second_category_tax.until = payroll_sencond_category_tax_inputs['until_2']
            payroll_second_category_tax.factor = payroll_sencond_category_tax_inputs['factor_2']
            payroll_second_category_tax.discount = payroll_sencond_category_tax_inputs['discount_2']
            payroll_second_category_tax.added_date = datetime.now()
            payroll_second_category_tax.updated_date = datetime.now()
            self.db.add(payroll_second_category_tax)
            self.db.commit()

            payroll_second_category_tax = PayrollSecondCategoryTaxModel()
            payroll_second_category_tax.period = payroll_sencond_category_tax_inputs['period']
            payroll_second_category_tax.since = payroll_sencond_category_tax_inputs['since_3']
            payroll_second_category_tax.until = payroll_sencond_category_tax_inputs['until_3']
            payroll_second_category_tax.factor = payroll_sencond_category_tax_inputs['factor_3']
            payroll_second_category_tax.discount = payroll_sencond_category_tax_inputs['discount_3']
            payroll_second_category_tax.added_date = datetime.now()
            payroll_second_category_tax.updated_date = datetime.now()
            self.db.add(payroll_second_category_tax)
            self.db.commit()

            payroll_second_category_tax = PayrollSecondCategoryTaxModel()
            payroll_second_category_tax.period = payroll_sencond_category_tax_inputs['period']
            payroll_second_category_tax.since = payroll_sencond_category_tax_inputs['since_4']
            payroll_second_category_tax.until = payroll_sencond_category_tax_inputs['until_4']
            payroll_second_category_tax.factor = payroll_sencond_category_tax_inputs['factor_4']
            payroll_second_category_tax.discount = payroll_sencond_category_tax_inputs['discount_4']
            payroll_second_category_tax.added_date = datetime.now()
            payroll_second_category_tax.updated_date = datetime.now()
            self.db.add(payroll_second_category_tax)
            self.db.commit()
            
            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"