from app.backend.db.models import OldMedicalLicenseModel, DocumentEmployeeModel, EmployeeModel
from datetime import datetime
from sqlalchemy import desc
from app.backend.classes.dropbox_class import DropboxClass
from app.backend.classes.helper_class import HelperClass
import json

class OldMedicalLicenseClass:
    def __init__(self, db):
        self.db = db

    def get(self, field, value, type=1, page=1, items_per_page=10):
        try:
            if type == 1:
                data = self.db.query(OldMedicalLicenseModel).filter(getattr(OldMedicalLicenseModel, field) == value).first()
                if data:
                    # Serializar el objeto OldMedicalLicenseModel a un diccionario
                    serialized_data = {
                        "document_employee_id": data.document_employee_id,
                        "document_type_id": data.document_type_id,
                        "folio": data.folio,
                        "since": data.since.strftime('%Y-%m-%d') if data.since else None,
                        "until": data.until.strftime('%Y-%m-%d') if data.until else None,
                        "days": data.days,
                        "support": data.support,
                        "status_id": data.status_id,
                        "id": data.id
                    }
                    return serialized_data
                else:
                    return "No data found"
            else:
                data_query = self.db.query(
                    OldMedicalLicenseModel.document_employee_id,
                    DocumentEmployeeModel.document_type_id,
                    OldMedicalLicenseModel.folio,
                    EmployeeModel.visual_rut,
                    OldMedicalLicenseModel.since,
                    OldMedicalLicenseModel.until,
                    OldMedicalLicenseModel.days,
                    DocumentEmployeeModel.support,
                    DocumentEmployeeModel.status_id,
                    OldMedicalLicenseModel.id
                ).outerjoin(DocumentEmployeeModel, DocumentEmployeeModel.id == OldMedicalLicenseModel.document_employee_id).outerjoin(EmployeeModel, EmployeeModel.rut == OldMedicalLicenseModel.rut).filter(getattr(OldMedicalLicenseModel, field) == value).filter(DocumentEmployeeModel.document_type_id == 35).order_by(desc(OldMedicalLicenseModel.since))

                total_items = data_query.count()
                total_pages = (total_items + items_per_page - 1) // items_per_page

                if page < 1 or page > total_pages:
                    return "Invalid page number"

                data = data_query.offset((page - 1) * items_per_page).limit(items_per_page).all()

                if not data:
                    return "No data found"

                # Serializar la lista de objetos OldMedicalLicenseModel a una lista de diccionarios
                serialized_data = {
                    "total_items": total_items,
                    "total_pages": total_pages,
                    "current_page": page,
                    "items_per_page": items_per_page,
                    "data": [
                        {
                            "document_employee_id": item.document_employee_id,
                            "document_type_id": item.document_type_id,
                            "folio": item.folio,
                            "visual_rut": item.visual_rut,
                            "since": item.since.strftime('%Y-%m-%d') if item.since else None,
                            "until": item.until.strftime('%Y-%m-%d') if item.until else None,
                            "days": item.days,
                            "support": item.support,
                            "status_id": item.status_id,
                            "id": item.id
                        }
                        for item in data
                    ]
                }

                serialized_result = json.dumps(serialized_data)

                return serialized_result
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, old_medicalLicense_inputs, ):
        try:
            medical_license = OldMedicalLicenseModel()
            medical_license.document_employee_id = old_medicalLicense_inputs['document_employee_id'],
            medical_license.medical_license_type_id = old_medicalLicense_inputs['medical_license_type_id']
            medical_license.patology_type_id = old_medicalLicense_inputs['patology_type_id']
            medical_license.period = old_medicalLicense_inputs['period']
            medical_license.rut = old_medicalLicense_inputs['rut']
            medical_license.folio = old_medicalLicense_inputs['folio']
            medical_license.since = old_medicalLicense_inputs['since']
            medical_license.until =old_medicalLicense_inputs['until']
            medical_license.days = old_medicalLicense_inputs['days']
            medical_license.added_date = datetime.now()
            medical_license.updated_date = datetime.now()
            self.db.add(medical_license)
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        