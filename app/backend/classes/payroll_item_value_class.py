from app.backend.db.models import PayrollItemValueModel
from datetime import datetime

class PayrollItemValueClass:
    def __init__(self, db):
        self.db = db

    def get_all(self, item_id = None, period = None):
        data = self.db.query(PayrollItemValueModel).filter(PayrollItemValueModel.item_id == item_id, PayrollItemValueModel.period == period).all()

        return data

    def get_with_period(self, rut, item_id, period):
        data = self.db.query(PayrollItemValueModel).filter(PayrollItemValueModel.rut == rut, PayrollItemValueModel.item_id == item_id, PayrollItemValueModel.period == period).first()

        return data
          
    def get(self, rut, taxable_id):
        data = self.db.query(PayrollItemValueModel).filter(PayrollItemValueModel.rut == rut, PayrollItemValueModel.item_id == taxable_id).first()

        return data
    
    def existence(self, rut, item_id, period):
        quantity = self.db.query(PayrollItemValueModel).filter(PayrollItemValueModel.rut == rut, PayrollItemValueModel.item_id == item_id, PayrollItemValueModel.period == period).count()

        return quantity
    
    def delete(self, rut, taxable_id):
        data = self.db.query(PayrollItemValueModel).filter(PayrollItemValueModel.rut == rut, PayrollItemValueModel.item_id == taxable_id).first()

        return data
    
    def store(self, data):
        quantity = self.existence(data['rut'], data['item_id'], data['period'])

        if quantity == 0:
            payroll_item_value = PayrollItemValueModel()
            payroll_item_value.rut = data['rut']
            payroll_item_value.item_id = data['item_id']
            payroll_item_value.period = data['period']
            payroll_item_value.amount = data['amount']
            payroll_item_value.added_date = datetime.now()
            payroll_item_value.updated_date = datetime.now()
            self.db.add(payroll_item_value)
            self.db.commit()
        else:
            self.update(data)

    def update(self, data):
        payroll_item_value = self.db.query(PayrollItemValueModel).filter(PayrollItemValueModel.rut == data['rut'], PayrollItemValueModel.item_id == data['item_id'], PayrollItemValueModel.period == data['period']).first()
        if payroll_item_value:
            payroll_item_value.amount = data['amount']
            payroll_item_value.updated_date = datetime.now()
            self.db.add(payroll_item_value)
            self.db.commit()
            return 1
        else:
            return "No data found"