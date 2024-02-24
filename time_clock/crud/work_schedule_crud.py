from sqlalchemy.orm import Session

from time_clock.database import models, schemas


def get_work_schedule_by_employee_id(db: Session, employee_id: int):
    return db.query(models.WorkSchedule).filter_by(employee_id=employee_id).first()


def create_work_schedule(db: Session, work_schedule: schemas.WorkScheduleCreate):
    db_work_schedule = models.WorkSchedule(work_days=work_schedule.work_days,
                                           work_hours=work_schedule.work_hours,
                                           start_time=work_schedule.start_time,
                                           employee_id=work_schedule.employee_id,
                                           calendar_id=work_schedule.calendar_id)

    db.add(db_work_schedule)
    db.commit()
    db.refresh(db_work_schedule)

    return db_work_schedule


def update_work_schedule(db: Session, employee_id: int, work_schedule: schemas.WorkScheduleUpdate):
    db_work_schedule = get_work_schedule_by_employee_id(db, employee_id)

    db_work_schedule.work_days = work_schedule.work_days
    db_work_schedule.work_hours = work_schedule.work_hours
    db_work_schedule.start_time = work_schedule.start_time

    db.add(db_work_schedule)
    db.commit()
    db.refresh(db_work_schedule)
    return db_work_schedule


def delete_work_schedule(db: Session, employee_id: int):
    db_team = get_work_schedule_by_employee_id(db, employee_id)

    db.delete(db_team)
    db.commit()
