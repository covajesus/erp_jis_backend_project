from app.backend.db.models import PayrollOtherIndicatorModel
from datetime import datetime

class PayrollOtherIndicatorClass:
    def __init__(self, db):
        self.db = db

    def get(self, period, other_type_id):
        data = self.db.query(PayrollOtherIndicatorModel).filter(PayrollOtherIndicatorModel.period == period).filter(PayrollOtherIndicatorModel.other_type_id == other_type_id).first()

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

    def store(self, payroll_indicator_inputs, other_type_id):
        try:
            if other_type_id == 1:
                payroll_other_indicator = PayrollOtherIndicatorModel()
                payroll_other_indicator.other_type_id = payroll_indicator_inputs['other_type_id']
                payroll_other_indicator.other_value = payroll_indicator_inputs['mutual_value']
                payroll_other_indicator.period = payroll_indicator_inputs['period']
                payroll_other_indicator.added_date = datetime.now()
                self.db.add(payroll_other_indicator)
                self.db.commit()

            if other_type_id == 2:
                payroll_other_indicator = PayrollOtherIndicatorModel()
                payroll_other_indicator.other_type_id = payroll_indicator_inputs['other_type_id']
                payroll_other_indicator.other_value = payroll_indicator_inputs['honorary_value']
                payroll_other_indicator.period = payroll_indicator_inputs['period']
                payroll_other_indicator.added_date = datetime.now()
                self.db.add(payroll_other_indicator)
                self.db.commit()

            if other_type_id == 3:
                payroll_other_indicator = PayrollOtherIndicatorModel()
                payroll_other_indicator.other_type_id = payroll_indicator_inputs['other_type_id']
                payroll_other_indicator.other_value = payroll_indicator_inputs['gratification_value']
                payroll_other_indicator.period = payroll_indicator_inputs['period']
                payroll_other_indicator.added_date = datetime.now()
                self.db.add(payroll_other_indicator)
                self.db.commit()

            inserted_id = payroll_other_indicator.id

            return inserted_id
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"