from datetime import datetime
import os
import pathlib
from tkinter.tix import COLUMN
from sqlalchemy import BLOB, create_engine, Table, MetaData, Column, Integer, String, select, insert
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import declarative_base

from config import DEFAULT_ENDTIME, DEFAULT_TIMEZONE

Base = declarative_base()

DB_NAME = "db.sqlite3"
DB_DIR = pathlib.Path(__file__).parent.parent.absolute() # Gets the parent path for the file for the creation of the file
DB_PATH = "sqlite:///" + str(DB_DIR / DB_NAME) # Create the path of the db

class Calendar(Base):
    """TODO: 
    ctag VARCHAR,
    orderindex INTEGER DEFAULT 0,
    hidden INTEGER DEFAULT 0,
    active INTEGER DEFAULT 0,
    last_checked INTEGER NOT NULL,
    supported_component_set INTEGER,
    """

    __tablename__ = "calendar"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    timezone = Column(String)
    created = Column(Integer)
    last_modified = Column(Integer)

class Events(Base):
    """TODO:
        alarm_id INTEGER,
        description LONGVARCHAR,
        all_day INTEGER,
        is_recurring INTEGER,
        start_recurring INTEGER,
        end_recurring INTEGER,
        location LONGVARCHAR,
        url LONGVARCHAR,
        etag LONGVARCHAR,
        href LONGVARCHAR,
        uid LONGVARCHAR,
        event_type_id INTEGER,
        task INTEGER,
        complete INTEGER,
        trash INTEGER,
        trash_time INTEGER,
        sequence INTEGER DEFAULT 0 NOT NULL,
        ical LONGVARCHAR,
        rrule LONGVARCHAR,
        organizer LONGVARCHAR,
        is_template INTEGER DEFAULT 0 NOT NULL,
        due INTEGER,
        priority INTEGER,
        status LONGVARCHAR,
        percentage_complete INTEGER,
        categories LONGVARCHAR,
        component_class LONGVARCHAR,
        attachment LONGVARCHAR,
        completed INTEGER,
        created INTEGER,
        last_modified INTEGER
    """

    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    calendar_id = Column(Integer, ForeignKey("calendar.id")) # Foreign Key
    title = Column(String)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    timezone = Column(String)
    ics = Column(BLOB)


def initialise():
    db = create_engine(DB_PATH)
    Base.metadata.create_all(db)
   
    db.connect()
    
    statement = select([True]).where(Calendar.id == 1).limit(1)
    results = db.execute(statement).fetchall()
    if (len(results)):
        return None
    insert_statement = insert(Calendar).values(title = "New Calendar", timezone = DEFAULT_TIMEZONE, created = datetime.now())
    db.execute(insert_statement)
    db.commit()

    """TODO: Add recurring events and notifications"""

