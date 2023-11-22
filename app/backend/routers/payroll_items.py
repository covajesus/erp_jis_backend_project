from fastapi import APIRouter, Depends, Form
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin, PayrollItem, PayrollItemList
from app.backend.classes.payroll_item_class import PayrollItemClass
from app.backend.auth.auth_user import get_current_active_user

payroll_items = APIRouter(
    prefix="/payroll_items",
    tags=["PayrollItems"]
)

@payroll_items.post("/")
def index(payroll_item_list: PayrollItemList, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db), items_per_page: int = 10):

    data = PayrollItemClass(db).get_all(payroll_item_list.page)

    return {"message": data}

@payroll_items.post("/store")
def store(payroll_item: PayrollItem, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    payroll_inputs = payroll_item.dict()
    data = PayrollItemClass(db).store(payroll_inputs)


    return {"message": data}

@payroll_items.delete("/delete/{id}")
def delete(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollItemClass(db).delete(id)

    return {"message": data}

@payroll_items.patch("/update/{id}")
def update(id:int, item_type_id: int = Form(...), item: str = Form(...), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    payroll_inputs = {"item_type_id": item_type_id, "item": item}
    data = PayrollItemClass(db).update(id, payroll_inputs)
    print(data)
    print(payroll_inputs)
    return {"message": data}

@payroll_items.get("/edit/{id}")
def get(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollItemClass(db).get(id)

    return {"message": data}