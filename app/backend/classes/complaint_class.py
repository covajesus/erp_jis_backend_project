from app.backend.db.models import ComplaintModel
from datetime import datetime

class ComplaintClass:
    def __init__(self, db):
        self.db = db
    
    def store(self, complaint_inputs):
        complaint = ComplaintModel()
        complaint.anonymous = complaint_inputs['anonymous']
        complaint.incident_date = complaint_inputs['incident_date']
        complaint.incident_place = complaint_inputs['incident_place']
        complaint.knowledge = complaint_inputs['knowledge']
        complaint.identify = complaint_inputs['identify']
        complaint.description = complaint_inputs['description']
        complaint.password = complaint_inputs['password']
        complaint.password_confirm = complaint_inputs['password_confirm']
        complaint.email = complaint_inputs['email']
        complaint.no_email = complaint_inputs['no_email']
        complaint.added_date = datetime.now()

        self.db.add(complaint)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    