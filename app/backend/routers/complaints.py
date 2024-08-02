from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Complaint, UserLogin
from app.backend.classes.complaint_class import ComplaintClass
from app.backend.auth.auth_user import get_current_active_user
from fastapi import UploadFile, File

complaints = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)

@complaints.post("/store")
def store(complaints:Complaint, support: UploadFile = File(...), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    complaints = complaints.dict()
    data = ComplaintClass(db).store(complaints)

    return {"message": data}