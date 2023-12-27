from app.backend.db.models import PayrollManualInputModel
from datetime import datetime

class PayrollManualInputClass:
    def __init__(self, db):
        self.db = db

    def store(self, manual_inputs_list):
        for item in manual_inputs_list:
            print(f"Payroll Item ID: {item.payroll_item_id}")
            print(f"RUT: {item.rut}")
            print(f"Amount Input: {item.amount_input}")
            print(f"Period: {item.period}")
            print("---")