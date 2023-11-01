from app.backend.db.models import  OldVacationModel
from datetime import datetime

class OldVacationClass:
    def __init__(self, db):
        self.db = db

    def get(self, field, value):
        try:
            data = self.db.query(OldVacationModel).filter(getattr(OldVacationModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, old_vacation_inputs):

        vacation = OldVacationModel()
        vacation.document_employee_id = old_vacation_inputs['document_employee_id']
        vacation.rut = old_vacation_inputs['rut']
        vacation.since = old_vacation_inputs['since']
        vacation.until = old_vacation_inputs['until']
        vacation.days = old_vacation_inputs['days']
        vacation.no_valid_days = old_vacation_inputs['no_valid_days']
        vacation.support = old_vacation_inputs['support']
        vacation.added_date = datetime.now()
        vacation.updated_date = datetime.now()

        self.db.add(vacation)
        try:
            self.db.commit()

            return 1
        except Exception as e:
            return 0
        