from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.payroll_calculation_class import PayrollCalculationClass
from app.backend.auth.auth_user import get_current_active_user

payroll_calculations = APIRouter(
    prefix="/payroll_calculations",
    tags=["PayrollCalculations"]
)

@payroll_calculations.get("/{period}")
def calculate(period:str, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollCalculationClass(db).calculate(period)

    return {"message": data}