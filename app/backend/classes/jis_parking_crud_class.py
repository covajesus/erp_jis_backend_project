from app.backend.db.models import JisParkingCrudModel
from datetime import datetime
from sqlalchemy import func
from app.backend.classes.helper_class import HelperClass
from app.backend.classes.dropbox_class import DropboxClass
import os
import json

class JisParkingCrudClass:
    def __init__(self, db):
        self.db = db

       
    def uploadImage(self, file):
        jis_parking_crud = JisParkingCrudModel()
        jis_parking_crud.support = file
        jis_parking_crud.updated_date = datetime.now()

        self.db.add(jis_parking_crud)
        self.db.commit()
        
        return 1
    
    def delete(self, id):
        data = self.db.query(JisParkingCrudModel).filter(JisParkingCrudModel.id == id ).first()
        support = data.support
        self.db.delete(data)
        self.db.commit()
        
        return support