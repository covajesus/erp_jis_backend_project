from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.db.models import EmployeeExtraModel
from app.backend.schemas import EmployeeExtra, UpdateEmployeeExtra, UserLogin
from app.backend.auth.auth_user import get_current_active_user
from app.backend.classes.employee_extra_datum_class import EmployeeExtraDatumClass


employee_extras = APIRouter(
    prefix="/employee_extras",
    tags=["Employee_Extras"]
)

@employee_extras.get("/")
def index(session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = db.query(EmployeeExtraModel).all()

    return {"message": data}

@employee_extras.post("/store")
def store(employee_extra:EmployeeExtra, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    employee_extra_inputs = employee_extra.dict()
    data = EmployeeExtraModel(**employee_extra_inputs)

    db.add(data)
    db.commit()

    return {"message": data}

@employee_extras.get("/edit/{rut}")
def edit(rut:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = db.query(EmployeeExtraModel).filter(EmployeeExtraModel.rut == rut).first()

    return {"message": data}

@employee_extras.delete("/delete/{id}")
def delete(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = EmployeeExtraDatumClass(db).delete(id)

    return {"message": data}

@employee_extras.patch("/update/{rut}")
def update(rut:int, employee:UpdateEmployeeExtra, session_user: UserLogin = Depends(get_current_active_user),  db: Session = Depends(get_db)):
    existing_employee = db.query(EmployeeExtraModel).filter(EmployeeExtraModel.rut == rut).one_or_none()

    if not existing_employee:
        return {"message": "Empleado no encontrado!"}

    existing_employee_data = employee.dict(exclude_unset=True)
    for key, value in existing_employee_data.items():
        setattr(existing_employee, key, value)

    db.commit()

    return {"message": "Empleado actualizado", "data": existing_employee}