import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base

# SQL Server URI compatible with SQLAlchemy
# SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://SA:Strong1passw0rd@localhost:1433/elevate_retail?driver=ODBC+Driver+18+for+SQL+Server;TrustServerCertificate=yes;'
SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://SA:Secure1passw0rd@127.0.0.1:1433/elevate_retail"
    "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)

# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()
