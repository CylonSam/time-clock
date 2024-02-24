from fastapi import FastAPI

from .routers import work_schedules_router, employees_router, teams_router, calendar_router

app = FastAPI(title="TimeClock")

app.include_router(teams_router.router)
app.include_router(employees_router.router)
app.include_router(calendar_router.router)
app.include_router(work_schedules_router.router)
