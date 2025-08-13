# ETL Mini Project – API to Database Pipeline

## Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline in Python.
It fetches weather data from the OpenWeatherMap API, processes it using Pandas, and stores it in a SQLite database.

## Files
- `etl_weather.py`: Fully functional version using OpenWeatherMap API and environment variables for API key.

## Steps
1. **Extract**: Fetch JSON data for a list of cities via OpenWeatherMap API.
2. **Transform**: Clean, format, and round temperature values.
3. **Load**: Store processed data in a SQLite database for querying.

## Technologies
- Python
- Pandas
- SQLite
- Requests
- Python-dotenv

## How to Run (Functional Version)
1. Install dependencies:
   ```bash
   pip install pandas requests python-dotenv
   ```
2. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
3. Copy `.env.example` to `.env` and replace `your_api_key_here` with your API key.
4. Run:
   ```bash
   python etl_weather.py
   ```

## Example Output
| city      | temp | feels_like | weather    | timestamp           |
|-----------|------|-----------|------------|---------------------|
| Frankfurt | 22.5 | 21.0      | clear sky  | 2025-08-11 14:00:00 |

## License
MIT License
