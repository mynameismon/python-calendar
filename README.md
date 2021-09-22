# PyCalendar

## Introduction, Objective and Scope
Calendars are ubiquitous. They are present in both physical and digital formats, with multiple clients available across all devices. 

Via this project, we propose making a simple, user friendly open-source calendar that can be used on any operating system supporting Python.

It shall aim to support the most widely used components (``VEVENT`` and ``VTODO``) along with it's properties, as specified in the widely supported [``icalendar`` specification](https://icalendar.org/RFC-Specifications/iCalendar-RFC-5545/). ``VJOURNAL`` is not planned to be supported at the moment. The application would also support importing and exporting ``.ics`` files. CalDAV support is also outside the scope of the project for the time being.

## Project Category 
RDBS/OOPS

## Process Description
The project would involve the usage of a SQLite3 database for storage and quick and easy access of data. Data would be called via a backend API. A GUI or a CLI would be built on top of the API to be expose the API to the user for a user-friendly interface.


## Future Scope and Enhancement
- Support for the entire ``icalendar`` specification
- Exposing the API via a command line interface for power users
- Support for CalDAV for web-based calendars (like Google Calendar and Microsoft Outlook)
