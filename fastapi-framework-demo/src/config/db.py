from sqlalchemy import create_engine, MetaData
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

# connect url
db_url = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(
    username=getenv("DB_USER"),
    password=getenv("DB_PASSWORD"),
    host=getenv("DB_HOST"),
    port=getenv("DB_PORT"),
    database=getenv("DB_NAME"),
)

# create the SQLAlchemy engine
# engine = create_engine(db_url, echo=True)
engine = create_engine(db_url)

meta_data = MetaData()

SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)
Base = declarative_base()
print("DB_URL", db_url)
print("ENGINE", engine)
# Base.metadata.drop_all(bind=engine)  # Elimina todas las tablas existentes (¡CUIDADO!)
Base.metadata.create_all(bind=engine)  # Crea las tablas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()