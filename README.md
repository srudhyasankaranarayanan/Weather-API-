# AI Weather Assistant Using Function Calling

### Live Link:  https://ktv96psmkzjjclkw8avmxa.streamlit.app/

## About the Project

AI Weather Assistant is a Streamlit-based application that provides
current weather information for any city.

The application uses Llama 3.1 8B Instruct with function calling.
The LLM requests the `get_weather()` Python function when weather
information is needed.

The Python function uses Open-Meteo APIs to find the city location
and retrieve current weather information.

## Features

* Current weather information
* LLM-based function calling
* Temperature
* Humidity
* Wind speed
* City location detection
* Streamlit web interface
* Open-Meteo API integration

## Technologies Used

* Python
* Streamlit
* Hugging Face
* Llama 3.1 8B Instruct
* Requests
* JSON
* Open-Meteo API
* Function Calling

## Project Flow

```text
User
  |
  v
Streamlit
  |
  v
Llama 3.1 8B Instruct
  |
  v
Function Calling
  |
  v
get_weather()
  |
  v
Open-Meteo Geocoding API
  |
  v
Latitude and Longitude
  |
  v
Open-Meteo Forecast API
  |
  v
Weather Data
  |
  v
Llama 3.1
  |
  v
Final Weather Report
```

## How It Works

1. The user enters a city name.
2. The question is sent to the LLM.
3. The LLM identifies the weather request.
4. The LLM creates a function call.
5. Python receives the city name.
6. `get_weather()` is executed.
7. Open-Meteo Geocoding API finds the city coordinates.
8. Open-Meteo Forecast API retrieves the current weather.
9. The weather data is returned to the LLM.
10. The LLM generates the final response.
11. Streamlit displays the weather information.

## Project Structure

```text
Weather-API-
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/srudhyasankaranarayanan/Weather-API-.git
```

Open the project:

```bash
cd Weather-API-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Hugging Face Token

Set the Hugging Face token as an environment variable:

```powershell
$env:HF_TOKEN="your_hugging_face_token"
```

Do not upload the token to GitHub.

## Run the Application

```bash
streamlit run app.py
```

Enter a city such as:

```text
Chennai
```

The application displays the current temperature, humidity,
wind speed, and AI-generated weather report.

## Function Calling

The main function used in this project is:

```python
get_weather(city)
```

The LLM requests this function when weather information is required.

Python executes the function and gets real weather information
from the Open-Meteo API.

The result is then sent back to the LLM for the final response.

## Future Improvements

* Multi-day weather forecast
* Weather alerts
* Weather icons
* Multiple-city comparison
* Voice-based questions
* Search history

## Conclusion

This project demonstrates how LLMs can use function calling to
connect with Python functions and external APIs.

It provides a practical understanding of LLMs, function calling,
API integration, Python, and Streamlit.

## Author

### Srudhya Sankaranarayanan  


