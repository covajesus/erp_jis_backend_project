from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.old_vacation_class import OldVacationClass
from app.backend.auth.auth_user import get_current_active_user
from app.backend.classes.vacation_class import VacationClass

old_vacations = APIRouter(
    prefix="/old_vacations",
    tags=["Old_Vacations"]
)

@old_vacations.post("/transfer/{rut}")
def transfer(rut: int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    vacations = VacationClass(db).get_all_with_no_pagination(rut)

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
        # VacationClass(db).delete(vacation.document_employee_id)

    return {"message": f"Datos de vacaciones transferidos para el RUT {rut}"}