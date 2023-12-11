from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Mesh,  UserLogin
from app.backend.classes.mesh_class import MeshClass
from app.backend.classes.helper_class import HelperClass
from app.backend.auth.auth_user import get_current_active_user


meshes = APIRouter(
    prefix="/meshes",
    tags=["Mesh"]
)


@meshes.post("/store")
def store(mesh:Mesh, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    mesh_inputs = mesh.dict()
    data = MeshClass(db).store(mesh_inputs)

    return {"message": data}

@meshes.get("/edit/{id}")
def edit(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = MeshClass(db).get("id", id)

    return {"message": data}

@meshes.get("/last_week_working_days/{rut}/{date}")
def last_week_working_days(rut:int, date:str , session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    dateSplit = HelperClass().split(str(date),'-' )
    data = MeshClass(db).last_week_working_days(rut, dateSplit[0], dateSplit[1])
    data = MeshClass(db).quantity_last_week_working_days(rut, dateSplit[0], dateSplit[1], data)
    

    return {"message": data}
