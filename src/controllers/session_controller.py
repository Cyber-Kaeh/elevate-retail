from src.models.session import Session
from src.utils.db_utils import get_session


def create_session(session_id, data):
    session = get_session()
    new_session = Session(session_id=session_id, data=data)
    session.add(new_session)
    session.commit()


def get_session_data(session_id):
    session = get_session()
    session_data = session.query(Session).filter(
        Session.session_id == session_id).first()
    return session_data


def update_session(session_id, data):
    session = get_session()
    session_data = session.query(Session).filter(
        Session.session_id == session_id).first()
    if session_data:
        session_data.data = data
        session.commit()


def delete_session(session_id):
    session = get_session()
    session_data = session.query(Session).filter(
        Session.session_id == session_id).first()
    if session_data:
        session.delete(session_data)
        session.commit()
