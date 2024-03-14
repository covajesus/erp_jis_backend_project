from fastapi import APIRouter, Depends, Request, Response, UploadFile, File
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import  UserLogin, UpdateContact
from app.backend.classes.employee_class import EmployeeClass
from app.backend.auth.auth_user import get_current_active_user
import base64
import os
from app.backend.classes.dropbox_class import DropboxClass
from app.backend.classes.contact_class import Contactclass
from app.backend.classes.helper_class import HelperClass
from fastapi import File, UploadFile
import dropbox

contact = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)

@contact.post("/send_email/") 
def send_email(request: Request, db: Session = Depends(get_db)):
    data = request.json()
    HelperClass().send_email(data)
    return {"message": "email sent successfully"}

@contact.patch("/update_contact/")
def update_contact(data: UpdateContact, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    Contactclass(db).update_contact(data)
    return {"message": "contact updated successfully"}

@contact.get("/get_contact/")
def get_contact(db: Session = Depends(get_db)):
    contact = Contactclass(db).get_contact()
    return contact

