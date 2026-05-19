import re

from transformers import pipeline
from app.utils.logger import get_logger
from app.utils.exception import SentimentPipelineError, PredictionError

logging = get_logger(__name__)

try:
    sentiment_pipeline = pipeline("sentiment-analysis")

except Exception as e:
    logging.error(f"Failed to load sentiment analysis pipeline: {e}")
    sentiment_pipeline = None

    raise SentimentPipelineError()



def predict_sentiment(text: str) -> dict:
    """
    Predict the sentiment of the input text.

    :param text: The input text to analyze.
    :return: A dictionary with the sentiment label and score.
    """

    if not sentiment_pipeline:
        raise SentimentPipelineError(
            "Sentiment analysis pipeline is not available."
        )

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    preprocessed_text = preprocess_input(text)

    logging.info(
        f"Preprocessed text for sentiment analysis: {preprocessed_text}"
    )

    try:
        result = sentiment_pipeline(preprocessed_text)[0]

        logging.info(f"Sentiment analysis result: {result}")

        return result

    except Exception as e:

        logging.error(f"Error during sentiment analysis: {e}")

        raise SentimentPipelineError(
            "Sentiment analysis failed."
        ) from e

def preprocess_input(text: str) -> str:
    """
    Preprocess the input text for sentiment analysis.
    """

    # lowercase and strip spaces
    text = text.lower().strip()

    # remove URLs
    text = re.sub(r"http\S+", "", text)

    # remove special characters
    text = re.sub(r"[^\w\s]", "", text)

    return text


def predict_sentiment(text: str) -> dict:

    if sentiment_pipeline is None:
        raise SentimentPipelineError(
            "Sentiment analysis pipeline is not available."
        )

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    preprocessed_text = preprocess_input(text)

    logging.info(
        f"Preprocessed text for sentiment analysis: {preprocessed_text}"
    )

    try:
        result = sentiment_pipeline(preprocessed_text)[0]

        logging.info(f"Sentiment analysis result: {result}")

        result['label'] = result['label'].lower()

        return result

    except Exception as e:
        logging.error(f"Error during sentiment analysis: {e}")

        raise SentimentPipelineError(
            "Sentiment analysis failed."
        ) from e