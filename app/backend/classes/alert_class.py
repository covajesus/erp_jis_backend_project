from app.backend.db.models import AlertModel
import json
from datetime import datetime

class AlertClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(AlertModel).order_by(AlertModel.id).all()
            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(AlertModel).filter(getattr(AlertModel, field) == value).first()

            if data:
                alert_data = data.as_dict()
                serialized_data = json.dumps(alert_data)

                return serialized_data

            else:
                return "No se encontraron datos para el campo especificado."

        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, alert_inputs):
        alert = AlertModel()
        alert.status_id = alert_inputs['status_id']
        alert.alert_type_id = alert_inputs['alert_type_id']
        alert.rut = alert_inputs['rut']
        alert.added_date = datetime.now()

        self.db.add(alert)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(AlertModel).filter(AlertModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, alert_inputs):
        alert =  self.db.query(AlertModel).filter(AlertModel.id == id).one_or_none()
        
        if 'alert_type_id' in alert_inputs and alert_inputs['alert_type_id'] is not None:
            alert.alert_type_id = alert_inputs['alert_type_id']

        if 'status_id' in alert_inputs and alert_inputs['status_id'] is not None:
            alert.rut = alert_inputs['status_id']

        if 'rut' in alert_inputs and alert_inputs['rut'] is not None:
            alert.rut = alert_inputs['rut']

        alert.update_date = datetime.now()

        self.db.add(alert)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            return 0