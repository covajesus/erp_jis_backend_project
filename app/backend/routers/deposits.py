from fastapi import APIRouter, Depends, UploadFile, File
from app.backend.schemas import UserLogin, SearchDeposit, StoreSupport
from app.backend.auth.auth_user import get_current_active_user
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.classes.deposit_class import DepositClass
from app.backend.classes.dropbox_class import DropboxClass
import os

deposits = APIRouter(
    prefix="/deposits",
    tags=["Deposits"]
)

@deposits.post("/{page}")
def index(search_data:SearchDeposit, page:int,  db: Session = Depends(get_db)):
    search_data = search_data.dict()

    data = DepositClass(db).get(search_data, page)

    return {"message": data}

@deposits.post("/store")
def store(form_data: StoreSupport = Depends(StoreSupport.as_form), picture: UploadFile = File(...), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    dropbox_client = DropboxClass(db)

    filename = dropbox_client.upload(name=form_data.rut, description='foto', data=picture,
                                 dropbox_path='/pictures/', computer_path=os.path.join(os.path.dirname(__file__)))

    data = DepositClass(db).store(form_data, filename)

    return {"message": data}