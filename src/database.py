from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, MappedAsDataclass
import os

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)

session = sessionmaker(bind=engine)


class Base(MappedAsDataclass, DeclarativeBase):
    pass
