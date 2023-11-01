from app.backend.db.models import UniformModel, UniformTypeModel
import json

class UniformClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(UniformModel).order_by(UniformModel.id).all()
            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(
                UniformModel.id,
                UniformModel.uniform_type_id,
                UniformModel.rut,
                UniformModel.delivered_date,
                UniformTypeModel.uniform_type
            ).\
            outerjoin(UniformTypeModel, UniformModel.uniform_type_id == UniformTypeModel.id).\
            filter(getattr(UniformModel, field) == value).\
            order_by(UniformModel.delivered_date.desc()).all()

            # Serializar los datos en formato JSON
            serialized_data = []
            for record in data:
                serialized_record = {
                    "id": record.id,
                    "uniform_type_id": record.uniform_type_id,
                    "rut": record.rut,
                    "delivered_date": record.delivered_date,
                    "uniform_type": record.uniform_type
                }
                serialized_data.append(serialized_record)

            return json.dumps(serialized_data)
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"

    def store(self, Uniform_inputs):
        try:
            data = UniformModel(**Uniform_inputs)
            self.db.add(data)
            self.db.commit()
            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(UniformModel).filter(UniformModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, bank):
        existing_bank = self.db.query(UniformModel).filter(UniformModel.id == id).one_or_none()

        if not existing_bank:
            return "No data found"

        existing_bank_data = bank.dict(exclude_unset=True)
        for key, value in existing_bank_data.items():
            setattr(existing_bank, key, value)

        self.db.commit()

        return 1