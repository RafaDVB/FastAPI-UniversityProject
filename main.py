from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine
from api.routes import router

def get_application():

    # Crear base de datos
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="API Proyecto 2", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Incluir rutas para los endpoint
    app.include_router(router, prefix="/music-store/api/v1")
    return app

app = get_application()

@app.get("/")
def home() -> dict:
    return {"mensaje": "Proyecto 2 - Rafael Villaseñor"}