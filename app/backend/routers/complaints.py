from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Complaint
from app.backend.classes.complaint_class import ComplaintClass
from fastapi import UploadFile, File
from app.backend.classes.dropbox_class import DropboxClass
import os

complaints = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)

@complaints.post("/store")
def store(complaints:Complaint = Depends(Complaint.as_form), support: UploadFile = File(...), db: Session = Depends(get_db)):
    complaints = complaints.dict()

    id = ComplaintClass(db).store(complaints)

    dropbox_client = DropboxClass(db)

    filename = dropbox_client.upload(name=id, description='complaint', data=support,
                                 dropbox_path='/complaints/', computer_path=os.path.join(os.path.dirname(__file__)))
    
    data =  ComplaintClass(db).update(id, filename)

    return {"message": data}