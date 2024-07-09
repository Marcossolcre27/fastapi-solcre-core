# mylibrary/crud_generator.py
from fastapi import FastAPI, HTTPException, Query, Depends
from typing import Type, List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session

def create_crud(app: FastAPI, model, create_schema: Type[BaseModel], read_schema: Type[BaseModel], endpoint_name: str, db_dependency):
    base_endpoint = f"/{endpoint_name}"
    all_endpoint = f"{base_endpoint}s"

    @app.post(base_endpoint, response_model=read_schema)
    def create(item: create_schema, db: Session = Depends(db_dependency)):
        db_item = model(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @app.get(all_endpoint, response_model=List[read_schema])
    def read_all(db: Session = Depends(db_dependency), sort: Optional[List[str]] = Query(None), **filters):
        query = db.query(model)
        for attr, value in filters.items():
            if value is not None:
                query = query.filter(getattr(model, attr) == value)
        if sort:
            for field in sort:
                desc = field.startswith('-')
                if desc:
                    query = query.order_by(getattr(model, field[1:]).desc())
                else:
                    query = query.order_by(getattr(model, field).asc())
        return query.all()

    @app.get(f"{base_endpoint}/{{item_id}}", response_model=read_schema)
    def read(item_id: int, db: Session = Depends(db_dependency)):
        db_item = db.query(model).filter(model.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{endpoint_name.capitalize()} not found")
        return db_item

    @app.put(f"{base_endpoint}/{{item_id}}", response_model=read_schema)
    def update(item_id: int, item: create_schema, db: Session = Depends(db_dependency)):
        db_item = db.query(model).filter(model.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{endpoint_name.capitalize()} not found")
        item_data = item.dict(exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        db.commit()
        return db_item

    @app.delete(f"{base_endpoint}/{{item_id}}", response_model=dict)
    def delete(item_id: int, db: Session = Depends(db_dependency)):
        db_item = db.query(model).filter(model.id == item_id).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail=f"{endpoint_name.capitalize()} not found")
        db.delete(db_item)
        db.commit()
        return {"message": f"{endpoint_name.capitalize()} with ID {item_id} has been deleted."}
