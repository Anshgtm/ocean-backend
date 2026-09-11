from sqlalchemy import Column, Integer, Float, Date, JSON
from app.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, nullable=False)

    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)

    depths = Column(JSON, nullable=False)
    temperature = Column(JSON, nullable=False)