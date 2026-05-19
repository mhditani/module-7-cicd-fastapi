from pydantic import BaseModel, ConfigDict


class Prediction(BaseModel):
    text: str
    sentiment: str

    model_config = ConfigDict(from_attributes=True)


class PredictionCreate(BaseModel):
    text: str