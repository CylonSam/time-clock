import logging

from sqlalchemy.orm import Session

from time_clock.database import models, schemas


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter_by(id=employee_id).first()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(name=employee.name,
                                  email=employee.email,
                                  leader=employee.leader,
                                  team_id=employee.team_id,
                                  hashed_password=employee.password,
                                  status=employee.status)

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    logging.info(f"New employee created! id={db_employee.id}")

    db_employee_time_bank = models.TimeBank(credit=0, debt=0, employee_id=db_employee.id)
    db.add(db_employee_time_bank)
    db.commit()
    db.refresh(db_employee_time_bank)

    return db_employee


def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeUpdate):
    db_employee = get_employee(db, employee_id)

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.hashed_password = employee.password
    db_employee.leader = employee.leader
    db_employee.status = employee.status

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)

    db.delete(db_employee)
    db.commit()
