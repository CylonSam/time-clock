# TimeClock [WIP]
Attempt at making an open-source, cool, beautiful, easy and FUNCTIONAL time clock that your company can host to micromanage you!

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- Alembic

## Requirements
- Docker / Docker Compose
- Python 3.11 / Pip

## How to run the app
1. Get app dependencies. Run `pip install -r requirements.txt` inside root directory.
2. Start the database. Run `docker compose up` inside **/deploy/local** directory.
3. Configure the database by running the migrations. Run `alembic upgrade head`.
4. Start the app. Run `python -m uvicorn time_clock.main:app --reload`

## API
TBA