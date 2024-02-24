from fastapi import APIRouter, Depends, HTTPException
from time_clock.database.database import SessionLocal
from time_clock.database import schemas
from time_clock.crud import team_crud
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/teams/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return team_crud.create_team(db=db, team=team)


@router.get("/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = team_crud.get_teams(db, skip=skip, limit=limit)
    return teams


@router.get("/teams/{team_id}", response_model=schemas.Team)
def read_team(team_id: int, db: Session = Depends(get_db)):
    db_team = team_crud.get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


@router.put("/teams/{team_id}", response_model=schemas.Team)
def update_team(team: schemas.TeamUpdate, team_id: int, db: Session = Depends(get_db)):
    db_team = team_crud.get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team_crud.update_team(db, team_id, team)


@router.delete("/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    db_team = team_crud.get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team_crud.delete_team(db, team_id)
