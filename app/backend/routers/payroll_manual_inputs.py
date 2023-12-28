from fastapi import APIRouter, Depends, Form, UploadFile, File, HTTPException
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import UserLogin, PayrollDataInput
from app.backend.classes.payroll_manual_input_class import PayrollManualInputClass
from app.backend.auth.auth_user import get_current_active_user
import pandas as pd

payroll_manual_inputs = APIRouter(
    prefix="/payroll_manual_inputs",
    tags=["PayrollManualInput"]
)

@payroll_manual_inputs.post("/store")
def store(payroll_manual_inputs: PayrollDataInput, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = PayrollManualInputClass(db).store(payroll_manual_inputs)

    return {"message": data}

@payroll_manual_inputs.post("/upload")
def upload(file: UploadFile = File(...), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    try:
        df = pd.read_excel(file.file, engine='openpyxl')
        payroll_manual_inputs = df.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo: {str(e)}")

    for usuario_data in usuarios_data:
        db_usuario = models.Usuario(**usuario_data)
        db.add(db_usuario)
    db.commit()