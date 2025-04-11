from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from src.config.db_config import DATABASE_URL
from contextlib import contextmanager

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Flask extensions
db = SQLAlchemy()
csrf = CSRFProtect()
session = Session()


@contextmanager
def get_session():
    sess = Session()
    try:
        yield sess
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(f"Database error!\nDatabase: {DATABASE_URL}\nError: {e}")
        raise
    finally:
        sess.close()
