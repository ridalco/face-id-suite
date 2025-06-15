from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id          = Column(Integer, primary_key=True, index=True)
    username    = Column(String(50), unique=True, index=True, nullable=False)
    email       = Column(String(120), unique=True, index=True, nullable=False)
    hashed_pwd  = Column(String(128), nullable=False)
    is_active   = Column(Boolean, default=True)
