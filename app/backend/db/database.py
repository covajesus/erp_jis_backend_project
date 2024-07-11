from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"

# Crear el motor con echo=True para activar el registro de consultas
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20, max_overflow=0, echo=False)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
