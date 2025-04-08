"""
src/models/base.py
This module contains the base class for all SQLAlchemy models in the project.
Import this in other model files to inherit from the base class.
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
