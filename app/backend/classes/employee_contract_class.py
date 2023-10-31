from app.backend.db.models import DocumentEmployeeModel, EmployeeModel
from sqlalchemy import desc
from app.backend.classes.dropbox_class import DropboxClass

class EmployeeContractClass:
    def __init__(self, db):
        self.db = db

    def get_all(self, rut):
        try:
            data = self.db.query(DocumentEmployeeModel.status_id, DocumentEmployeeModel.added_date, DocumentEmployeeModel.support, DocumentEmployeeModel.rut, DocumentEmployeeModel.id, EmployeeModel.visual_rut, EmployeeModel.names, EmployeeModel.father_lastname, EmployeeModel.mother_lastname). \
                        outerjoin(EmployeeModel, EmployeeModel.id == DocumentEmployeeModel.rut). \
                        filter(DocumentEmployeeModel.rut == rut). \
                        filter(DocumentEmployeeModel.document_type_id == 21). \
                        order_by(desc(DocumentEmployeeModel.id)). \
                        all()
            
            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    
    def download(self, id):
        try:
            data = self.db.query(DocumentEmployeeModel).filter(DocumentEmployeeModel.id == id).first()

            file = DropboxClass(self.db).get('/employee_contracts/', data.support)

            return file
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"