from app.backend.db.models import EmployeeExtraModel

class EmployeeExtraDatumClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(EmployeeExtraModel).order_by(EmployeeExtraModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(EmployeeExtraModel).filter(getattr(EmployeeExtraModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, employee_extra_datum_inputs):
        try:
            data = EmployeeExtraModel(**employee_extra_datum_inputs)
            self.db.add(data)
            self.db.commit()
            return "Registro agregado"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(EmployeeExtraModel).filter(EmployeeExtraModel.rut == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, employee_extra_datum):
        existing_employee_extra_datum = self.db.query(EmployeeExtraModel).filter(EmployeeExtraModel.id == id).one_or_none()

        if not existing_employee_extra_datum:
            return "No se encontró el registro"

        existing_employee_extra_datum_data = employee_extra_datum.dict(exclude_unset=True)
        for key, value in existing_employee_extra_datum_data.items():
            setattr(existing_employee_extra_datum, key, value)

        self.db.commit()

        return "Registro actualizado"