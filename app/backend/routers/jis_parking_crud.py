from fastapi import APIRouter, Depends, Request, Response, UploadFile, File
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Employee, UpdateEmployee, SearchEmployee, UserLogin, EmployeeList, UploadSignature, UploadPicture
from app.backend.classes.employee_class import EmployeeClass
from app.backend.auth.auth_user import get_current_active_user
import base64
import os
from app.backend.classes.dropbox_class import DropboxClass
from app.backend.classes.jis_parking_crud_class import JisParkingCrudClass
from fastapi import File, UploadFile
import dropbox

jis_parking_crud = APIRouter(
    prefix="/jis_parking_crud",
    tags=["Jis_Parking_Crud"]
)

@jis_parking_crud.post("/upload_image/")
def upload_image(support: UploadFile = File(...) , session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    print(support)
    dropbox_client = DropboxClass(db)

    filename = dropbox_client.upload(name=support.filename, data=support, dropbox_path='/JisParking_assets/', computer_path=os.path.join(os.path.dirname(__file__)), resize=0)

    JisParkingCrudClass(db).uploadImage(filename)
    return {"message": "File uploaded successfully", "file_name": filename}

@jis_parking_crud.delete("/delete_image/{id}")
def delete_image(id: int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    dropbox_client = DropboxClass(db)
    support = JisParkingCrudClass(db).delete(id)
    # Get the file from the request
    # Delete the file from Dropbox
    dropbox_client.delete("/JisParking_assets/",support)

    return {"message": "File deleted successfully"}
