# TimeClock
Attempt at making an open-source, cool, beautiful, easy and FUNCTIONAL time clock that your company can host to micromanage you!

## Requirements
- Docker / Docker Compose
- Python 3.11 / Pip

## How to run the app
1. Start the database. Run `docker compose up` inside **/deploy/local** directory.
2. Get app dependencies. Run `pip install -r requirements.txt` inside root directory.
3. Start the app. Run `python -m uvicorn time_clock.main:app --reload`

## API
TBA