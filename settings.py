from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///batch.db", echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
