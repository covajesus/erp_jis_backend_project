from fastapi import APIRouter, Depends, File, UploadFile
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import FamilyCoreDatum, UserLogin
from app.backend.classes.old_family_core_datum_class import OldFamilyCoreDatumClass
from app.backend.db.models import FamilyCoreDatumModel
from app.backend.auth.auth_user import get_current_active_user
import os
from app.backend.classes.dropbox_class import DropboxClass
from app.backend.classes.family_core_datum_class import FamilyCoreDatumClass
from typing import Optional
from sqlalchemy import delete

old_family_core_data = APIRouter(
    prefix="/old_family_core_data",
    tags=["Old_Family_Core_Data"]
)





@old_family_core_data.post("/transfer/{employee_rut}")
def transfer_family_core_data(employee_rut: int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    # Obtén los datos del núcleo familiar del empleado
    family = db.query(FamilyCoreDatumModel).filter(FamilyCoreDatumModel.employee_rut == employee_rut).all()
    
    # Inserta los datos en old_family_core_data
    for datum in family:
        old_datum_inputs = {
            'family_type_id': datum.family_type_id,
            'employee_rut': datum.employee_rut,
            'gender_id': datum.gender_id,
            'employee_rut': datum.rut,
            'names': datum.names,
            'father_lastname': datum.father_lastname,
            'mother_lastname': datum.mother_lastname,
            'born_date': datum.born_date,
            'support': datum.support,
        }
        print(datum.employee_rut, datum.names)
        OldFamilyCoreDatumClass(db).store(old_datum_inputs)

    # Elimina los datos de family
    # delete_statement = delete(FamilyCoreDatumModel).where(FamilyCoreDatumModel.employee_rut == employee_rut)
    # db.execute(delete_statement)

    db.commit()

    return {"message": f"Datos del núcleo familiar transferidos para el RUT {employee_rut}"}

@old_family_core_data.get("/edit/{rut}/{get_type_id}")
def edit(rut:int, get_type_id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):

    data = OldFamilyCoreDatumClass(db).get("employee_rut", rut, get_type_id)

    return {"message": data}
