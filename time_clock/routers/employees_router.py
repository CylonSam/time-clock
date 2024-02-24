from fastapi import APIRouter, Depends, HTTPException
from time_clock.database.database import SessionLocal
from time_clock.database import schemas
from time_clock.crud import employee_crud
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/employees/", response_model=schemas.EmployeeBase)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return employee_crud.create_employee(db=db, employee=employee)


@router.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return employee_crud.get_employees(db, skip=skip, limit=limit)


@router.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = employee_crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee: schemas.EmployeeUpdate, employee_id: int, db: Session = Depends(get_db)):
    db_employee = employee_crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_crud.update_employee(db, employee_id, employee)


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = employee_crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_crud.delete_employee(db, employee_id)
