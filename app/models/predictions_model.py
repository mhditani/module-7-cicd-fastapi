from app.database import Base, engine
from sqlalchemy import Column, Integer, String, Float

class Predictions(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    prediction = Column(String, index=True)
