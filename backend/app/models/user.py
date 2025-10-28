from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Integer, default=1)
    role = Column(String, default="user") # e.g. admin, triage, user