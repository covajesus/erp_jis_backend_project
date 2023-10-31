from fastapi import APIRouter, Depends, Response, UploadFile, File
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.old_vacation_class import OldVacationClass
from app.backend.classes.document_employee_class import DocumentEmployeeClass
from app.backend.auth.auth_user import get_current_active_user
import os
import requests
from fastapi.responses import JSONResponse

old_vacations = APIRouter(
    prefix="/old_vacations",
    tags=["Old_Vacations"]
)




@old_vacations.get("/total_vacation_days_in_company")
def total_vacation_days_in_company(session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = OldVacationClass(db).calculate_total_vacation_days()

    return {"message": data}

from app.backend.db.models import VacationModel
from app.backend.classes.vacation_class import VacationClass
from sqlalchemy import delete

@old_vacations.post("/transfer/{rut}")
def transfer_vacations(rut: int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    # Obtén los datos de las vacaciones del empleado
    vacations = db.query(VacationModel).filter(VacationModel.rut == rut).all()

    # Inserta los datos en old_vacations
    for vacation in vacations:
        old_vacation_inputs = {
            'document_employee_id': vacation.document_employee_id,
            'rut': vacation.rut,
            'since': vacation.since,
            'until': vacation.until,
            'days': vacation.days,
            'no_valid_days': vacation.no_valid_days,
            'support': vacation.support,
        }
        OldVacationClass(db).store(old_vacation_inputs)

    # Elimina los datos de vacations
    delete_statement = delete(VacationModel).where(VacationModel.rut == rut)
    db.execute(delete_statement)

    db.commit()

    return {"message": f"Datos de vacaciones transferidos para el RUT {rut}"}