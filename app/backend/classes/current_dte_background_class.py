import requests
from sqlalchemy.orm import Session
from app.backend.db.models import CurrentDteBackgroundModel

class CurrentDteBackgroundClass:
    def __init__(self, db):
        self.db = db
    
    def delete(self, folio):
        try:
            data = self.db.query(CurrentDteBackgroundModel).filter(CurrentDteBackgroundModel.folio == folio).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"