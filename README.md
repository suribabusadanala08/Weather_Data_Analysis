# Weather Data Analysis System

A starter Flask application with HTML, CSS and JavaScript frontend, state-wise weather summaries, Chart.js graphs, SQLite authentication and parameterized database queries.

## Requirements
- Python 3.10+
- Internet connection in the browser for Chart.js CDN (or download Chart.js locally for offline use)

## Windows setup (CMD)
```bat
cd Weather_Data_Analysis_System
py -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
python app.py
```
Open http://127.0.0.1:5000

## First use
1. Register a user.
2. Sign in.
3. Select a state/UT and date range in the dashboard.
4. View average metrics and charts.

## Dataset
`data/raw/india_weather_dataset.csv` contains clearly-labelled **synthetic demonstration records** for a representative city in each of India's 28 states and 8 union territories. They are not observed or official weather reports. Replace these records with a verified historical dataset or connect a trusted weather provider before presenting results as real measurements.

Expected CSV columns:
`state,city,date,temperature,humidity,rainfall,wind_speed,pressure,weather_condition`

## Security notes
- Passwords are hashed using Werkzeug.
- SQL statements use placeholders / parameterized values.
- Flask-WTF CSRF protection is enabled for POST forms.
- Session cookies are HttpOnly and SameSite=Lax. Set `COOKIE_SECURE=true` behind HTTPS.
- Change `SECRET_KEY` in `.env`; never commit `.env`.
- This is a development starter, not a production deployment. Add HTTPS, rate limiting, email verification, password reset delivery, logging, backups and a production WSGI server before deployment.

## Project structure
- `frontend/`: Jinja templates, CSS and browser JavaScript
- `backend/`: routes, services, models and security helpers
- `database/`: SQLite initialization and schema
- `data/`: raw and processed CSV files
- `analysis/`: reusable data analysis functions
- `tests/`: starter tests
