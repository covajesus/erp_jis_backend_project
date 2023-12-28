from fastapi import APIRouter, Depends, Form
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin, PayrollDataInput
from app.backend.classes.payroll_manual_input_class import PayrollManualInputClass
from app.backend.auth.auth_user import get_current_active_user

payroll_manual_inputs = APIRouter(
    prefix="/payroll_manual_inputs",
    tags=["PayrollManualInput"]
)

@payroll_manual_inputs.post("/store")
def store(payroll_manual_inputs: PayrollDataInput, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollManualInputClass(db).store(payroll_manual_inputs)

    return {"message": data}