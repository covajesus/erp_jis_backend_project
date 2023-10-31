from fastapi import APIRouter, Depends, File, UploadFile
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.medical_license_class import MedicalLicenseClass
from app.backend.auth.auth_user import get_current_active_user
from app.backend.db.models import MedicalLicenseModel
from app.backend.classes.old_medical_license_class import OldMedicalLicenseClass
from sqlalchemy import delete

import os

old_medical_licenses = APIRouter(
    prefix="/old_medical_licenses",
    tags=["OldMedicalLicenses"]
)

@old_medical_licenses.post("/transfer/{rut}")
def transfer_medical_licenses(rut: int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    # Obtén los datos de las licencias médicas del empleado
    medical_licenses = db.query(MedicalLicenseModel).filter(MedicalLicenseModel.rut == rut).all()

    # Inserta los datos en old_medical_licenses
    for medical in medical_licenses:
        old_license_inputs = {
            'document_employee_id': medical.document_employee_id,
            'medical_license_type_id': medical.medical_license_type_id,
            'patology_type_id': medical.patology_type_id,
            'period': medical.period,
            'rut': medical.rut,
            'folio': medical.folio,
            'since': medical.since,
            'until': medical.until,
            'days': medical.days,
        }
        OldMedicalLicenseClass(db).store(old_license_inputs)

    # Elimina los datos de medical_licenses
    delete_statement = delete(MedicalLicenseModel).where(MedicalLicenseModel.rut == rut)
    db.execute(delete_statement)

    db.commit()

    return {"message": f"Datos de licencias médicas transferidos para el RUT {rut}"}

@old_medical_licenses.get("/edit/{rut}/{page}")
def edit(rut:int, page:int = None, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = MedicalLicenseClass(db).get("rut", rut, 2, page)
    
    return {"message": data}