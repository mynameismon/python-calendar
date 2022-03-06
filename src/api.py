from tkinter import Event
import sqlalchemy as sqla
from sqlalchemy import or_, select
from sqlalchemy.orm import Session
import datetime
from src.db import DB_PATH, Events, Calendar

try:
    from ..config import DEFAULT_TIMEZONE, TODAY, DEFAULT_ENDTIME
except (ImportError, ValueError):
    import sys
    sys.path.append("..")
    from config import DEFAULT_TIMEZONE, TODAY, DEFAULT_ENDTIME

def get_events(start_date=TODAY, end_date=DEFAULT_ENDTIME):
    db_engine = sqla.create_engine(DB_PATH)
    db_engine.connect()

    try:
        statement = select(
            [Events.title, Events.start, Events.end, Events.timezone]
        ).where(or_(Events.start >= start_date, Events.end <= end_date))
        results = db_engine.execute(statement).fetchall()
        return results

    except Exception as e:
        raise e
    
def insert_events(title, start_date, end_date, timezone = DEFAULT_TIMEZONE, calendar = 1):
    db_engine = sqla.create_engine(DB_PATH)
    db_engine.connect()
    try:
        with Session(db_engine) as db_sessions:
            new_event = Events(calendar_id = calendar, title = title, start = start_date, end = end_date, timezone= timezone)
            db_sessions.add(new_event)
            db_sessions.commit()

    except Exception as e:
        raise e
