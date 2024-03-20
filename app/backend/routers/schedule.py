from typing import Optional
from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin
from app.backend.classes.schedule_class import ScheduleClass
from app.backend.schemas import CreateSchedule
from app.backend.auth.auth_user import get_current_active_user

schedule = APIRouter(
    prefix="/schedule",
    tags=["Schedule"]
)

@schedule.post("/store")
def store(data:CreateSchedule, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    print(data.horary_name)
    data = ScheduleClass(db).store(data)

    return {"message": data}


@schedule.get("/get_all")
def get_all(session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = ScheduleClass(db).get_all()

    return {"message": data}

@schedule.get("/get_by_group/{group_id}/{search_term}")
def get_by_group(group_id:int, search_term: Optional[str] = None, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = ScheduleClass(db).get_by_group_from_week_schedule(group_id, search_term)

    return {"message": data}

@schedule.get("/get_by_week_schedule_id/{id}")
def get_by_week_schedule_id(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = ScheduleClass(db).get_by_week_schedule_id(id)

    return {"message": data}