from app.backend.db.models import PayrollOtherIndicatorModel
from datetime import datetime

class PayrollOtherIndicatorClass:
    def __init__(self, db):
        self.db = db

    def get(self, period):
        data = self.db.query(PayrollOtherIndicatorModel).filter(PayrollOtherIndicatorModel.period == period).first()

        return data

    def get_all(self, period):
        try:
            data = self.db.query(PayrollOtherIndicatorModel).filter(PayrollOtherIndicatorModel.period == period).first()
            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"

    def store(self, payroll_indicator_inputs):
        try:
            payroll_other_indicator = PayrollOtherIndicatorModel()
            payroll_other_indicator.mutual_value = payroll_indicator_inputs['mutual_value']
            payroll_other_indicator.added_date = datetime.now()
            self.db.add(payroll_other_indicator)
            self.db.commit()

            inserted_id = payroll_other_indicator.id

            return inserted_id
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"