# 🌦️ Weather Forecast App

A clean and responsive Weather Forecast web application. It provides current weather conditions and a 5-day/3-hour forecast using a Flask-powered backend API that fetches data from the OpenWeatherMap API.

[cite_start]The application backend is built with performance and security in mind, featuring response caching (via `Flask-Caching`)  [cite_start]and API rate-limiting (via `Flask-Limiter`).

## 📸 Screenshots

Here's a look at the application's user interface.

**Search Page:** The user can search for any city by name.
<img width="1895" height="1030" alt="image" src="https://github.com/user-attachments/assets/b776bd65-cf2b-438b-87d6-b677c41aeae0" />


**Current Weather:** Displays the main weather card with temperature, humidity, and wind speed.
<img width="1877" height="1032" alt="image" src="https://github.com/user-attachments/assets/b0397895-8e46-49fb-a0e1-f18e6d45d152" />


**Forecast:** Shows the upcoming forecast for the selected location.
<img width="1884" height="1031" alt="image" src="https://github.com/user-attachments/assets/606a6e6c-d953-47a7-89fc-cde265a4c0cb" />


## ✨ Features

* **Current Weather:** Get real-time weather data for any city (by name) or coordinates (latitude/longitude).
* **Full Day Forecast:** Retrieve a Full day forecast, provided in 3-hour intervals.
* **Backend Caching:** API responses are cached (default 600 seconds) to reduce calls to the OpenWeatherMap API and improve response speed.
* **Rate Limiting:** The API is protected from abuse with a default rate limit of 60 requests per minute per IP.
* **Clean RESTful API:** A simple API powers the frontend, making it easy to manage or extend.

## 🛠️ Tech Stack

* [cite_start]**Backend:** Flask 
* [cite_start]**API Client:** `requests` 
* [cite_start]**Caching:** `Flask-Caching` 
* [cite_start]**Rate Limiting:** `Flask-Limiter` 
* [cite_start]**Configuration:** `python-dotenv` 
* **Data Source:** [OpenWeatherMap API](https://openweathermap.org/api)
* [cite_start]**Dependencies:** `pytest` (for testing) 

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### 1. Prerequisites

* [cite_start]Python 3.12+ 
* `pip` (Python package installer)
* An API key from [OpenWeatherMap](https://openweathermap.org/api)

### 2. Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/weather-forecast-app.git](https://github.com/your-username/weather-forecast-app.git)
    cd weather-forecast-app
    ```

2.  **Create and activate a virtual environment:**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    The `requirements.txt` file contains all necessary packages.
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuration

The application uses a `.env` file to manage environment variables. [cite_start]This file is ignored by Git[cite: 1].

1.  Create a file named `.env` in the root of the project.
2.  [cite_start]Add the following content to it, based on the provided example `.env` file[cite: 2].

    ```ini
    # Get your API key from [https://openweathermap.org/api](https://openweathermap.org/api)
    OWM_API_KEY=YOUR_OPENWEATHERMAP_API_KEY_HERE
    
    # Set the Flask environment (development or production)
    FLASK_ENV=development
    FLASK_APP=app.py
    
    # Set the cache timeout in seconds
    CACHE_TIMEOUT=600
    ```

3.  [cite_start]**Important:** Replace `YOUR_OPENWEATHERMAP_API_KEY_HERE` with your actual OpenWeatherMap API key[cite: 2].

### 4. Running the Application

With your virtual environment active and `.env` file configured, you can start the Flask server.

```bash
flask run
