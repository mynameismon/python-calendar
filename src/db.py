import os
import pathlib
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql.schema import ForeignKey, MetaData

DB_NAME = "db.sqlite3"
DB_DIR = pathlib.Path(__file__).parent.parent.absolute() # Gets the parent path for the file for the creation of the file
DB_PATH = "sqlite:///" + str(DB_DIR / DB_NAME) # Create the path of the db

def initialise():
    db = create_engine(DB_PATH)
    try:
        db = create_engine(DB_PATH)
        db.connect()
        db.execute("SELECT 1;")
    except OperationalError:
        db.create_engine(DB_PATH)
    meta = MetaData()
        
    # Creating the schema for the db
    calendar = Table("calendar",meta,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("description", String),
        Column("timezone", String),
        Column("created", Integer),
        Column("last_modified", Integer)
    )
    calendar.create(db, checkfirst=True)
    """TODO: 
    ctag VARCHAR,
    orderindex INTEGER DEFAULT 0,
    hidden INTEGER DEFAULT 0,
    active INTEGER DEFAULT 0,
    last_checked INTEGER NOT NULL,
    supported_component_set INTEGER,
    """

    events = Table("events", meta,
        Column("id", Integer, primary_key=True),
        Column("calendar_id", Integer, ForeignKey("calendar.id")), # Foreign Key
        Column("title", String),
        Column("start", Integer, nullable=False),
        Column("end", Integer, nullable=False),
        Column("timezone", String)
    )
    events.create(db, checkfirst=True)
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

    """TODO: Add recurring events and notifications"""

