# Tasks

- make calendar
  - events

```sql
CREATE TABLE calendar(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name LONGVARCHAR,
  description LONGVARCHAR,
  ctag VARCHAR,
  orderindex INTEGER DEFAULT 0,
  hidden INTEGER DEFAULT 0,
  active INTEGER DEFAULT 0,
  last_checked INTEGER NOT NULL,
  timezone LONGVARCHAR,
  supported_component_set INTEGER,
  created INTEGER,
  last_modified INTEGER
);
CREATE TABLE events(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  calendar_id INTEGER,
  alarm_id INTEGER,
  title LONGVARCHAR,
  description LONGVARCHAR,
  start INTEGER NOT NULL,
  end INTEGER NOT NULL,
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
  timezone LONGVARCHAR,
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
);
CREATE TABLE recurring_exceptions( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  parent_event_id INTEGER NOT NULL,
  exception_event_id INTEGER NOT NULL,
  exception_day INTEGER,
  cancelled INTEGER,
  created INTEGER,
  last_modified INTEGER
);
CREATE TABLE notifications( // if we have time
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id INTEGER,
  name LONGVARCHAR,
  description LONGVARCHAR,
  when_time INTEGER NOT NULL,
  period INTEGER,
  delay INTEGER,
  created INTEGER,
  last_modified INTEGER
); 
```