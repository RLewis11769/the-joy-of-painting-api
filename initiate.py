from engine.db import SessionLocal
from sqlalchemy.orm import Session


def get_db():
    Session = SessionLocal()
    try:
        yield Session
    finally:
        Session.close()
