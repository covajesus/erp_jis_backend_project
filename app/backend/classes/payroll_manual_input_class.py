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
    
    def multiple_store(self, payroll_manual_inputs):
        numeric_rut = HelperClass().numeric_rut(str(payroll_manual_inputs.rut))

        payroll_manual_input = PayrollManualInputModel()
        payroll_manual_input.rut = numeric_rut
        payroll_manual_input.payroll_item_id = payroll_manual_inputs.payroll_item_id
        payroll_manual_input.amount = payroll_manual_inputs.amount
        payroll_manual_input.period = payroll_manual_inputs.period
        payroll_manual_input.added_date = datetime.now()

        self.db.add(payroll_manual_input)

        self.db.commit()

        return 1