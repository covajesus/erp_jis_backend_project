from app.backend.db.models import EmployeeLaborDatumModel
from app.backend.classes.helper_class import HelperClass

class ContractDataClass:
    def __init__(self, db):
        self.db = db

    def first_expiration(self, expiration_inputs):
        try:
            data = self.db.query(EmployeeLaborDatumModel).filter(EmployeeLaborDatumModel.rut == expiration_inputs['rut']).first()

            response = HelperClass.extention_contract(data.entrance_company)

            if not data:
                return "No data found"
            return response
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def second_expiration(self, first_expiration):
        try:
            response = HelperClass.extention_contract(first_expiration)

            return response
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"