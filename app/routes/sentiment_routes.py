from fastapi import APIRouter

from app.schemas.predictions_schema import (
    Prediction,
    PredictionCreate
)

from app.services.sentiment_service import (
    predict_sentiment as sentiment_predict
)

router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment Analysis"]
)


@router.post("/predict", response_model=Prediction)
def predict_sentiment_route(
    prediction: PredictionCreate,
):
    """
    Predict the sentiment of the input text.

    :param prediction: The input text to analyze.
    :return: Sentiment prediction result.
    """

    result = sentiment_predict(prediction.text)

    return Prediction(
        text=prediction.text,
        sentiment=result["label"]
    )