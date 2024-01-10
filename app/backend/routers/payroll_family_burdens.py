from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.payroll_family_burden_class import PayrollFamilyBurdenClass
from app.backend.auth.auth_user import get_current_active_user

payroll_family_burdens = APIRouter(
    prefix="/payroll_family_burdens",
    tags=["PayrollFamilyBurdens"]
)

@payroll_family_burdens.get("/{section_id}/{period}")
def index(section_id:int, period:str, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollFamilyBurdenClass(db).get(section_id, period)

    return {"message": data}