import os
import joblib

from app.utils.exception import InvalidInputError
from app.utils.logger import get_logger
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



MODEL_PATH = os.path.join("app", "models", "iris_model.pkl")

logger = get_logger(__name__)



def train_model():
    try:
        logger.info("Starting model training...")

        # Load the iris dataset
        iris = load_iris()
        X, y = iris.data, iris.target
        logger.debug("Dataset loaded successfully")

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        logger.info("Dataset split into training and testing sets")

        # Create model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        logger.debug("Model initialized")

        # Train model
        model.fit(X_train, y_train)
        logger.info("Model training completed")

        # Ensure models folder exists
        model_dir = os.path.join("app", "models")
        os.makedirs(model_dir, exist_ok=True)

        # Save model
        model_path = os.path.join(model_dir, "iris_model.pkl")
        joblib.dump(model, model_path)

        logger.info(f"Model saved at {model_path}")

    except FileNotFoundError as error:
        logger.error(f"File not found: {error}")

    except Exception as e:
        logger.exception(f"Unexpected error during training: {e}")


if __name__ == "__main__":
    train_model()



def load_model():
    try:
        logger.info(f"Loading model from {MODEL_PATH}")
        model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully")
        return model

    except FileNotFoundError:
        logger.error(f"Model file not found at {MODEL_PATH}")
        raise

    except Exception as e:
        logger.exception(f"Error loading model: {e}")
        raise
    
    
    


def predict(input_data):
    try:
        logger.debug(f"Received input: {input_data}")

        # Validate input
        if not input_data or len(input_data[0]) != 4:
            message = (
                "Input must contain exactly 4 features: "
                "sepal length, sepal width, petal length, petal width."
            )
            logger.error(message)
            raise InvalidInputError(message)

        # Load model
        model = load_model()

        # Predict
        prediction = model.predict(input_data)
        result = prediction[0]

        logger.info(f"Prediction successful: {result}")

        return result

    except InvalidInputError as e:
        logger.warning(f"Invalid input: {e}")
        return None

    except ValueError as e:
        logger.error(f"Value error during prediction: {e}")
        return None

    except Exception as e:
        logger.exception(f"Unexpected error during prediction: {e}")
        return None
    
    
    
    def add_predictions_to_db(db: Session, input_data: list[float], prediction: float):
        try:
            from app.models.predictions_model import Prediction

            new_prediction = Prediction(
                sepal_length=input_data[0][0],
                sepal_width=input_data[0][1],
                petal_length=input_data[0][2],
                petal_width=input_data[0][3],
                predicted_class=prediction
            )
            db.add(new_prediction)
            db.commit()
            db.refresh(new_prediction)
            logger.info("Prediction added to database successfully")
            return new_prediction

        except Exception as e:
            logger.exception(f"Error adding prediction to database: {e}")
            raise