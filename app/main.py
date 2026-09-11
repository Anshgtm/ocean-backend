from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.prediction import router as prediction_router
from app.database import Base, engine
from app.models.prediction import Prediction

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ocean Temperature Reconstruction API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router)

@app.get("/")
def root():
    return {
        "message": "Ocean Backend is running",
        "status": "ok"
    }