from app.schemas.item_schema import ItemSchema
from app.utils.exception import InvalidInputError, ItemNotFoundError
from app.models.item_model import  Item
from sqlalchemy.orm import Session
"""
Example:

input: 1, name: "Item1", value: 10.0

db[1] = Item(id=1, name="Item1", value=10.0)
db[2] = Item(id=2, name="Item2", value=20.0)

{
    "id": 1,
    "item": Item(id=1, name="Item1", value=10.0)
},
{
    "id": 2,
    "item": Item(id=2, name="Item2", value=20.0)
}
"""

# Fake in-memory database
# db: dict[int, Item] = {}


# def create_item(item: Item):
#     db[item.id] = item
#     return item

# def create_item(db: Session, item: ItemSchema):
#     db_item = Item(name=item.name, value=item.value)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# def get_item(item_id: int) -> Item:
#     if item_id not in db:
#         raise ItemNotFoundError(item_id)

#     return db[item_id]


# def update_item(item_id: int, item: Item) -> Item:
#     if item_id not in db:
#         raise ItemNotFoundError(item_id)

#     db[item_id] = item
#     return item

# def delete_item(item_id: int) -> None:
#     if item_id not in db:
#         raise ItemNotFoundError(f'Item with id {item_id} not found.')

#     return db.pop[item_id]

# def list_items() -> list[Item]:
#     return list(db.values())    





from sqlalchemy.orm import Session

from app.models.item_model import Item
from app.schemas.item_schema import ItemSchema


def create_item(db: Session, item: ItemSchema):
    db_item = Item(
        name=item.name,
        value=item.value
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def list_items(db: Session):
    return db.query(Item).all()


def update_item(db: Session, item_id: int, item: ItemSchema):
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        return None

    db_item.name = item.name
    db_item.value = item.value

    db.commit()
    db.refresh(db_item)

    return db_item


def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        return None

    db.delete(db_item)
    db.commit()

    return db_item 