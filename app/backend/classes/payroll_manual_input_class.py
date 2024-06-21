from app.backend.db.models import PayrollManualInputModel
from app.backend.classes.payroll_class import PayrollClass
from app.backend.classes.payroll_item_value_class import PayrollItemValueClass
from app.backend.classes.helper_class import HelperClass
from datetime import datetime

class PayrollManualInputClass:
    def __init__(self, db):
        self.db = db

    def store(self, manual_inputs_list):
        for payroll_manual_input in manual_inputs_list.payroll_employees:
            rut = payroll_manual_input.rut
            payroll_item_id = payroll_manual_input.payroll_item_id
            amount = payroll_manual_input.amount
            period = payroll_manual_input.period

            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = payroll_item_id
            payroll_item_value_data['rut'] = rut
            payroll_item_value_data['period'] = period
            payroll_item_value_data['amount'] = amount

            PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return 1
    
    def get(self, rut, item_id, period):
        data = self.db.query(PayrollManualInputModel). \
                        filter(PayrollManualInputModel.rut == rut, PayrollManualInputModel.period == period, PayrollManualInputModel.item_id == item_id).first()

        if data:
            return {
                'rut': data.rut,
                'item_id': data.item_id,
                'period': data.period,
                'amount': data.amount
            }
        else:
            return None
    
    def multiple_store(self, payroll_manual_inputs):
        numeric_rut = HelperClass().numeric_rut(str(payroll_manual_inputs.rut))

        existence_status = PayrollItemValueClass(self.db).existence(numeric_rut, payroll_manual_inputs.payroll_item_id, payroll_manual_inputs.period)

        if existence_status > 0 and existence_status != None:
            PayrollItemValueClass(self.db).delete_with_period(numeric_rut, payroll_manual_inputs.payroll_item_id, payroll_manual_inputs.period)

            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = payroll_manual_inputs.payroll_item_id
            payroll_item_value_data['rut'] = numeric_rut
            payroll_item_value_data['period'] = payroll_manual_inputs.period
            payroll_item_value_data['amount'] = payroll_manual_inputs.amount

            PayrollItemValueClass(self.db).store(payroll_item_value_data)
        else:
            payroll_item_value_data = {}
            payroll_item_value_data['item_id'] = payroll_manual_inputs.payroll_item_id
            payroll_item_value_data['rut'] = numeric_rut
            payroll_item_value_data['period'] = payroll_manual_inputs.period
            payroll_item_value_data['amount'] = payroll_manual_inputs.amount

            PayrollItemValueClass(self.db).store(payroll_item_value_data)

        return 1