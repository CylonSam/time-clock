from fastapi import APIRouter, Depends, HTTPException
from time_clock.database.database import SessionLocal
from time_clock.database import schemas
from time_clock.crud import work_schedule_crud
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/work_schedules/", response_model=schemas.WorkSchedule)
def create_work_schedule(work_schedule: schemas.WorkScheduleCreate, db: Session = Depends(get_db)):
    return work_schedule_crud.create_work_schedule(db=db, work_schedule=work_schedule)


@router.get("/work_schedules/", response_model=schemas.WorkSchedule)
def read_work_schedule_by_employee_id(employee_id: int, db: Session = Depends(get_db)):
    return work_schedule_crud.get_work_schedule_by_employee_id(db=db, employee_id=employee_id)


@router.put("/work_schedules/{employee_id}", response_model=schemas.WorkSchedule)
def update_work_schedule(employee_id: int, work_schedule: schemas.WorkScheduleUpdate, db: Session = Depends(get_db)):
    db_work_schedule = work_schedule_crud.get_work_schedule_by_employee_id(db, employee_id)
    if db_work_schedule is None:
        raise HTTPException(status_code=404, detail="Work schedule not found")
    return work_schedule_crud.update_work_schedule(db, employee_id, work_schedule)


@router.delete("/work_schedules/{employee_id}")
def delete_work_schedule(employee_id: int, db: Session = Depends(get_db)):
    db_work_schedule = work_schedule_crud.get_work_schedule_by_employee_id(db, employee_id)
    if db_work_schedule is None:
        raise HTTPException(status_code=404, detail="Work schedule not found")
    return work_schedule_crud.delete_work_schedule(db, employee_id)
