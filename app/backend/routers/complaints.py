from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Complaint, VerifyComplaint
from app.backend.classes.complaint_class import ComplaintClass
from fastapi import UploadFile, File, Form
from app.backend.classes.dropbox_class import DropboxClass
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

complaints = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)

from typing import Optional
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
import os

@complaints.post("/store")
def store(complaints: Complaint = Depends(Complaint.as_form), support: Optional[UploadFile] = File(None), db: Session = Depends(get_db)):
    complaints = complaints.dict()

    id = ComplaintClass(db).store(complaints)

    if support:
        dropbox_client = DropboxClass(db)
        filename = dropbox_client.upload(name=id, description='complaint', data=support,
                                         dropbox_path='/complaints/', computer_path=os.path.join(os.path.dirname(__file__)))
        data = ComplaintClass(db).update(id, filename)


        send_email(id, complaints, "contacto@jisparking.com")
        send_email(id, complaints, "patriciogomez@jisparking.com")
    else:
        send_email(id, complaints, "contacto@jisparking.com")
        send_email(id, complaints, "patriciogomez@jisparking.com")

        data = ''

    return {"message": data}

def send_email(id, complaint_data: dict, recipient: str):
    sender_email = "no-reply@jisparking.com"
    sender_password = "Noreply2024!"
    subject = "Canal de Denuncias - Detalles de la Denuncia"

    html_template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Detalles de la Denuncia</title>
    </head>
    <body>
        <h1>Detalles de la Denuncia</h1>
        <table border="1" cellpadding="10" cellspacing="0">
            <tr>
                <td>N° de Denuncia</td>
                <td>${id}</td>
            </tr>
            <tr>
                <td>¿Cuál es su relación con Jisparking SpA?</td>
                <td>${relationship}</td>
            </tr>
            <tr>
                <td>Lugar donde sucedió el incidente:</td>
                <td>${incident_place}</td>
            </tr>
            <tr>
                <td>Tipo de Denuncia</td>
                <td>${complaint_type}</td>
            </tr>
            <tr>
                <td>¿Desea permanecer en el anonimato para esta denuncia?</td>
                <td>${anonymous}</td>
            </tr>
            <tr>
                <td>¿En qué fecha sucedió el incidente?</td>
                <td>${incident_date}</td>
            </tr>
            <tr>
                <td>¿Dónde sucedió la infracción?</td>
                <td>${incident_place_detail}</td>
            </tr>
            <tr>
                <td>¿Cómo tomó conocimiento de este hecho?</td>
                <td>${knowledge}</td>
            </tr>
            <tr>
                <td>¿Puede identificar a las personas comprometidas en esta infracción?</td>
                <td>${identify}</td>
            </tr>
            <tr>
                <td>Descripción</td>
                <td>${description}</td>
            </tr>
            <tr>
                <td>Correo</td>
                <td>${email}</td>
            </tr>
        </table>
    </body>
    </html>
    """)

    # Substitute the placeholders with actual values
    html_content = html_template.substitute(
        id=id,
        relationship=complaint_data.get('relationship', 'N/A'),
        incident_place=complaint_data.get('incident_place', 'N/A'),
        complaint_type=complaint_data.get('complaint_type', 'N/A'),
        anonymous=complaint_data.get('anonymous', 'N/A'),
        incident_date=complaint_data.get('incident_date', 'N/A'),
        incident_place_detail=complaint_data.get('incident_place_detail', 'N/A'),
        knowledge=complaint_data.get('knowledge', 'N/A'),
        identify=complaint_data.get('identify', 'N/A'),
        description=complaint_data.get('description', 'N/A'),
        password=complaint_data.get('password', 'N/A'),
        email=complaint_data.get('email', 'N/A')
    )

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP_SSL('mail.jisparking.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

@complaints.post("/verify")
def store(id: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):

    data = ComplaintClass(db).verify({"id": id, "password": password})

    return {"message": data}