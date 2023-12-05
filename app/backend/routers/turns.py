from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.turn_class import TurnClass
from app.backend.auth.auth_user import get_current_active_user

turns = APIRouter(
    prefix="/turns",
    tags=["Turn"]
)

@turns.get("/edit/{employee_type_id}/{group_id}/{search_term}")
def edit(employee_type_id:int, group_id:int, search_term:str = None, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = TurnClass(db).get(employee_type_id, group_id, search_term)

    return {"message": data}
