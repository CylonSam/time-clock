from fastapi import APIRouter, Depends, HTTPException
from time_clock.database.database import SessionLocal
from time_clock.database import schemas
from time_clock.crud import calendar_crud
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/calendars/", response_model=schemas.CalendarBase)
def create_calendar(calendar: schemas.CalendarCreate, db: Session = Depends(get_db)):
    return calendar_crud.create_calendar(db, calendar)


@router.get("/calendars/{calendar_id}", response_model=schemas.CalendarBase)
def get_calendar(calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = calendar_crud.get_calendar_by_id(db, calendar_id)
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return db_calendar


@router.get("/calendars/", response_model=list[schemas.CalendarBase])
def get_calendar(db: Session = Depends(get_db)):
    return calendar_crud.get_calendars(db)


@router.get("/calendars/", response_model=schemas.CalendarBase)
def get_calendar(city: str, state: str, db: Session = Depends(get_db)):
    db_calendar = calendar_crud.get_calendar_by_city_and_state(db, city, state)
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return db_calendar


@router.put("/calendars/{calendar_id}", response_model=schemas.CalendarBase)
def update_calendar(calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = calendar_crud.get_calendar_by_id(db, calendar_id)
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return calendar_crud.update_calendar(db, db_calendar)


@router.delete("/calendars/{calendar_id}")
def delete_calendar(calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = calendar_crud.get_calendar_by_id(db, calendar_id)
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return calendar_crud.delete_calendar(db, calendar_id)
