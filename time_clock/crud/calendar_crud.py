from sqlalchemy.orm import Session

from time_clock.database import models, schemas


def create_calendar(db: Session, calendar: schemas.CalendarCreate):
    db_calendar = models.Calendar(city=calendar.city, state=calendar.state)

    db.add(db_calendar)
    db.commit()
    db.refresh(db_calendar)

    return db_calendar


def get_calendars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Calendar).offset(skip).limit(limit).all()


def get_calendar_by_id(db: Session, calendar_id: int):
    return db.query(models.Calendar).filter_by(id=calendar_id).first()


def get_calendar_by_city_and_state(db: Session, city: str, state: str):
    return db.query(models.Calendar).filter_by(city=city, state=state).first()


def update_calendar(db: Session, calendar_id: int, calendar: schemas.CalendarUpdate):
    db_calendar = get_calendar_by_id(db, calendar_id)

    db_calendar.city = calendar.city
    db_calendar.state = calendar.state

    db.add(db_calendar)
    db.commit()
    db.refresh(db_calendar)

    return db_calendar


def delete_calendar(db: Session, calendar_id: int):
    db_calendar = get_calendar_by_id(db, calendar_id)

    db.delete(db_calendar)
    db.commit()
