from fastapi import FastAPI
from .routers import employees, teams

app = FastAPI(title="TimeClock")

app.include_router(employees.router)
app.include_router(teams.router)
