# models.py
from fastapi_framework_core.models import BaseModel


from sqlalchemy import Column, Integer, String

class User(BaseModel):
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
