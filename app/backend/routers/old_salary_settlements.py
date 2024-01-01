from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin, SalarySettlement
from app.backend.classes.salary_settlement_class import SalarySettlementClass
from app.backend.auth.auth_user import get_current_active_user
from fastapi import UploadFile, File
import os
from app.backend.classes.dropbox_class import DropboxClass
from typing import List

old_salary_settlements = APIRouter(
    prefix="/old_salary_settlements",
    tags=["OldSalarySettlements"]
)

@old_salary_settlements.get("/edit/{rut}/{page}")
def edit(rut:int, page:int = None, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = OldSalarySettlementClass(db).get("rut", rut, 2, page)

    return {"message": data}