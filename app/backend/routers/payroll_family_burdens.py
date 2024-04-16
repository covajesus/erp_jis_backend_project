from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin, UploadFamilyBurden
from app.backend.classes.payroll_family_burden_class import PayrollFamilyBurdenClass
from app.backend.auth.auth_user import get_current_active_user
from fastapi import UploadFile, File, HTTPException
import pandas as pd
import io

payroll_family_burdens = APIRouter(
    prefix="/payroll_family_burdens",
    tags=["PayrollFamilyBurdens"]
)

@payroll_family_burdens.get("/{section_id}/{period}")
def index(section_id:int, period:str, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollFamilyBurdenClass(db).get(section_id, period)

    return {"message": data}

@payroll_family_burdens.post("/upload")
async def upload(form_data: UploadFamilyBurden = Depends(UploadFamilyBurden.as_form), file: UploadFile = File(...), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    try:
        file_content = await file.read()
        file_bytesio = io.BytesIO(file_content)
        df = pd.read_excel(file_bytesio, engine='openpyxl', usecols=['Rut', 'Monto'])
        payroll_manual_input_data = df.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo: {str(e)}")

    for payroll_manual_input in payroll_manual_input_data:
        
        for key, value in payroll_manual_input.items():
            if key == 'Rut':
                form_data.rut = value
            if key == 'Tramo':
                form_data.section = value
            if key == 'N° Cargas':
                form_data.burden = value
            if key == 'Monto Familiar':
                form_data.family_amount = value
            if key == 'Monto Retroactivo':
                form_data.retroactive_amount = value

        PayrollFamilyBurdenClass(db).multiple_store(form_data)

    return 1