import json
from sqlalchemy import desc
from app.backend.db.models import  OldDocumentEmployeeModel, OldVacationModel
from datetime import datetime

class OldVacationClass:
    def __init__(self, db):
        self.db = db

    def get_all(self, rut):
        try:
            data_query = self.db.query(OldVacationModel).filter(OldVacationModel.rut == rut)

            data = data_query.all()

            if not data:
                return "No data found"

            serialized_data = [
                {
                    "rut": item.rut,
                    "id": item.id,
                    "since": item.since.strftime('%Y-%m-%d') if item.since else None,
                    "until": item.until.strftime('%Y-%m-%d') if item.until else None,
                    "days": item.days,
                    "no_valid_days": item.no_valid_days
                }
                for item in data
            ]

            serialized_result = json.dumps(serialized_data)

            return serialized_result
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
        