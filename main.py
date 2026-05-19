# from fastapi import FastAPI, HTTPException
# from app.utils.exception import InvalidInputError
# from app.utils.logger import get_logger
# from app.routes.crud_routes import router as crud_router
# from app.routes.ml_routes import router as ml_router
# from app.database import Base, engine


# logger = get_logger(__name__)
# logger.info("Starting model training...")

# app = FastAPI(title="Iris flower prediction API")
# app.include_router(crud_router)

# app.include_router(ml_router)

# Base.metadata.create_all(bind=engine)


# @app.get('/')
# async def root():
#     return {"message": "Welcome to the Iris flower prediction API"}



from fastapi import FastAPI

from app.utils.logger import get_logger
from app.routes.crud_routes import router as crud_router
from app.routes.ml_routes import router as ml_router
from app.database import Base, engine
from app.models.item_model import Item
from app.routes.sentiment_routes import router as sentiment_router


logger = get_logger(__name__)
logger.info("Starting application...")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Iris flower prediction API")

app.include_router(crud_router)
app.include_router(ml_router)
app.include_router(sentiment_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Iris flower prediction API"}