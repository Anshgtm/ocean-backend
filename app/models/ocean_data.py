from sqlalchemy import Column, Integer, Float, Date
from app.database import Base


class OceanData(Base):
    __tablename__ = "ocean_data"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, nullable=False)

    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)

    sst = Column(Float)
    sss = Column(Float)
    ssh = Column(Float)

    current_u = Column(Float)
    current_v = Column(Float)

    wind_u = Column(Float)
    wind_v = Column(Float)