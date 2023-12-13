from app.backend.db.models import MeshModel
from sqlalchemy import desc, asc
from sqlalchemy import extract
import json
from app.backend.db.models import MeshModel

class MeshClass:
    def __init__(self, db):
        self.db = db

    
    def quantity_last_week_working_days(self, rut, year, month, dataLastWeek):
                data_dict = json.loads(dataLastWeek)
                try:
                    data = self.db.query(MeshModel)\
                        .filter(MeshModel.rut == rut)\
                        .filter(extract('year', MeshModel.date) == year)\
                        .filter(extract('month', MeshModel.date) == month)\
                        .filter(MeshModel.week_id == data_dict['week_id'] )\
                        .count()      
                    return data
                except Exception as e:
                    error_message = str(e)
                    return f"Error: {error_message}"
      
    def last_week_working_days(self, rut, year, month):
        try:
            data = self.db.query(MeshModel)\
                .filter(MeshModel.rut == rut)\
                .filter(extract('year', MeshModel.date) == year)\
                .filter(extract('month', MeshModel.date) == month)\
                .order_by(desc(MeshModel.week_id))\
                .first()      
            
            if data:
                # Serializar el objeto MeshModel a un diccionario
                mesh_data = {
                    'id': data.id,
                    'turn_id': data.turn_id,
                    'week_id': data.week_id,
                    'rut': data.rut,
                    'date': data.date.strftime("%Y-%m-%d"),
                    'added_date': data.added_date.strftime("%Y-%m-%d"),  # Convert the datetime object to a string format
                }

                # Convierte el diccionario a una cadena JSON
                serialized_data = json.dumps(mesh_data)

                return serialized_data
            else:
                return "No se encontraron datos para el campo especificado."

        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"

    def get(self, field, value):
        try:
            data = self.db.query(MeshModel).filter(getattr(MeshModel, field) == value).first()

            if data:
                # Serializar el objeto MeshModel a un diccionario
                mesh_data = {
                    'id': data.id,
                    'turn_id': data.turn_id,
                    'week_id': data.week_id,
                    'rut': data.rut,
                    'added_date': data.added_date.strftime("%Y-%m-%d"), 
                }


                # Convierte el diccionario a una cadena JSON
                serialized_data = json.dumps(mesh_data)

                return serialized_data

            else:
                return "No se encontraron datos para el campo especificado."

        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, Mesh_inputs):
        try:
            data = MeshModel(**Mesh_inputs)
            self.db.add(data)
            self.db.commit()
            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"