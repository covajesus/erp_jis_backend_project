from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.db.models import OldEmployeeExtraModel
from app.backend.schemas import OldEmployeeExtra,UserLogin
from app.backend.auth.auth_user import get_current_active_user

old_employee_extras = APIRouter(
    prefix="/old_employee_extras",
    tags=["Old_Employee_Extras"]
)


@old_employee_extras.post("/store")
def store(old_employee_extra:OldEmployeeExtra, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    old_employee_extra_inputs = old_employee_extra.dict()
    data = OldEmployeeExtraModel(**old_employee_extra_inputs)

    db.add(data)
    db.commit()

    return {"message": data}

@old_employee_extras.get("/edit/{rut}")
def edit(rut:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = db.query(OldEmployeeExtraModel).filter(OldEmployeeExtraModel.rut == rut).first()

    return {"message": data}
