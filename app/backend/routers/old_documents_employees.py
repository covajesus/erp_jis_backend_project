from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import OldDocumentEmployee, UserLogin
from app.backend.classes.old_document_employee_class import OldDocumentEmployeeClass
from app.backend.classes.document_employee_class import DocumentEmployeeClass
from app.backend.classes.dropbox_class import DropboxClass
import os
from app.backend.auth.auth_user import get_current_active_user
from app.backend.db.models import DocumentEmployeeModel, OldDocumentEmployeeModel
from sqlalchemy import delete


old_documents_employees = APIRouter(
    prefix="/old_documents_employees",
    tags=["OldDocumentsEmployees"]
)


@old_documents_employees.post("/transfer/{rut}")
def transfer_documents(rut: int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    # Obtén los documentos del empleado
    documents = db.query(DocumentEmployeeModel).filter(DocumentEmployeeModel.rut == rut).all()

    # Inserta los documentos en old_documents_employees
    for doc in documents:
        old_doc_inputs = {
            'status_id': doc.status_id,
            'document_type_id': doc.document_type_id,
            'rut': doc.rut,
            'support': doc.support,
        }
        OldDocumentEmployeeClass(db).store(old_doc_inputs)

    # Elimina los documentos de documents_employees
    delete_statement = delete(DocumentEmployeeModel).where(DocumentEmployeeModel.rut == rut)
    db.execute(delete_statement)

    db.commit()

    return {"message": f"Documentos transferidos para el RUT {rut}"}

@old_documents_employees.get("/edit/{rut}")
def edit(rut:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = OldDocumentEmployeeClass(db).get("rut", rut)

    return {"message": data}
