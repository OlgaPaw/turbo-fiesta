import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTRGES_LOCAL = 'postgres://postgres:mysecretpassword@postgres:5432'
SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', POSTRGES_LOCAL)

postgres_args = {'sslmode': 'allow'} if os.environ.get('DATABASE_URL') else {}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=postgres_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
