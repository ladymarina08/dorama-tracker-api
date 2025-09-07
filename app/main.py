from fastapi import FastAPI
from app import routes
from app.database import Base, engine
from app import models

app = FastAPI(
    title='Dorama Tracker API',
    description='API para registrar doramas assistidos',
    version='1.0.0'
)

app.include_router(routes.router)
models.Base.metadata.create_all(bind=engine)