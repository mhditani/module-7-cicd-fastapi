# from fastapi import APIRouter, HTTPException, Depends    
# from app.schemas.item_schema import ItemSchema
# from app.services.crud_services import create_item, get_item, update_item, delete_item, list_items
# from app.utils.exception import InvalidInputError, ItemNotFoundError
# from sqlalchemy.orm import Session
# router = APIRouter(prefix="/items", tags=["items"])
# from app.dependencies import get_db


# # Post localhost:8000/items/ with body {"id": 1, "name": "Item1", "value": 10.0}
# @router.post("/", response_model=ItemSchema)
# def create_item_route(item: ItemSchema, db: Session = Depends(get_db)):
#     try:
#         return create_item(db, item)
#     except InvalidInputError as e:
#         raise HTTPException(status_code=400, detail=e.message)
    
    
    
    
# @router.get("/{item_id}", response_model=ItemSchema)
# def get_item_route(item_id: int):   
#     try:
#         return get_item(item_id)
#     except ItemNotFoundError as e:
#         raise HTTPException(status_code=404, detail=e.message)    
    
    
# @router.put("/{item_id}", response_model=ItemSchema)
# def update_item_route(item_id: int, item: ItemSchema):
#     try:
#         return update_item(item_id, item)
#     except ItemNotFoundError as e:
#         raise HTTPException(status_code=404, detail=e.message)    
    
    
# @router.delete("/{item_id}")
# def delete_item_route(item_id: int):
#     try:
#         delete_item(item_id)
#         return {"message": f"Item with id {item_id} deleted successfully."}
#     except ItemNotFoundError as e:
#         raise HTTPException(status_code=404, detail=e.message)    


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.item_schema import ItemSchema
from app.services.crud_services import (
    create_item,
    get_item,
    update_item,
    delete_item,
    list_items,
)
from app.utils.exception import InvalidInputError, ItemNotFoundError
from app.dependencies import get_db


router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemSchema)
def create_item_route(item: ItemSchema, db: Session = Depends(get_db)):
    try:
        return create_item(db, item)
    except InvalidInputError as e:
        raise HTTPException(status_code=400, detail=e.message)


@router.get("/", response_model=list[ItemSchema])
def list_items_route(db: Session = Depends(get_db)):
    return list_items(db)


@router.get("/{item_id}", response_model=ItemSchema)
def get_item_route(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Item with id {item_id} not found."
        )

    return item


@router.put("/{item_id}", response_model=ItemSchema)
def update_item_route(
    item_id: int,
    item: ItemSchema,
    db: Session = Depends(get_db)
):
    updated_item = update_item(db, item_id, item)

    if updated_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Item with id {item_id} not found."
        )

    return updated_item


@router.delete("/{item_id}")
def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    deleted_item = delete_item(db, item_id)

    if deleted_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Item with id {item_id} not found."
        )

    return {"message": f"Item with id {item_id} deleted successfully."}