import json
import requests
import streamlit as st
from groq import Groq


st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌤️",
    layout="centered"
)


st.title("🌤️ AI Weather Assistant")
st.write("Ask about the current weather of any city.")


GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(
    api_key=GROQ_API_KEY
)


MODEL = "llama-3.1-8b-instant"


def get_weather(city):

    location_response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "format": "json"
        },
        timeout=10
    )

    location_data = location_response.json()

    if "results" not in location_data:
        return {
            "error": "City not found"
        }

    location = location_data["results"][0]

    weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        },
        timeout=10
    )

    weather_data = weather_response.json()["current"]

    return {
        "city": location["name"],
        "country": location.get("country", ""),
        "temperature": weather_data["temperature_2m"],
        "humidity": weather_data["relative_humidity_2m"],
        "wind_speed": weather_data["wind_speed_10m"]
    }


weather_tool = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


city = st.text_input(
    "🏙️ Enter a city",
    placeholder="Example: Chennai"
)


if st.button("🌤️ Get Weather"):

    if not city.strip():
        st.warning("Please enter a city.")
        st.stop()

    messages = [
        {
            "role": "user",
            "content": f"What is the current weather in {city}?"
        }
    ]

    with st.spinner("Checking weather..."):

        try:

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=weather_tool,
                tool_choice="auto"
            )

            assistant_message = response.choices[0].message

            if assistant_message.tool_calls:

                tool_call = assistant_message.tool_calls[0]

                arguments = json.loads(
                    tool_call.function.arguments
                )

                requested_city = arguments["city"]

                weather = get_weather(requested_city)

                messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_message.content,
                        "tool_calls": [
                            {
                                "id": tool_call.id,
                                "type": "function",
                                "function": {
                                    "name": tool_call.function.name,
                                    "arguments": tool_call.function.arguments
                                }
                            }
                        ]
                    }
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(weather)
                    }
                )

                final_response = client.chat.completions.create(
                    model=MODEL,
                    messages=messages
                )

                st.subheader("🤖 AI Weather Report")

                st.write(
                    final_response.choices[0].message.content
                )

                st.subheader("📊 Weather Details")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "🌡️ Temperature",
                        f"{weather['temperature']} °C"
                    )

                with col2:
                    st.metric(
                        "💧 Humidity",
                        f"{weather['humidity']}%"
                    )

                with col3:
                    st.metric(
                        "💨 Wind Speed",
                        f"{weather['wind_speed']} km/h"
                    )

            else:

                st.write(assistant_message.content)

        except Exception as error:

            st.error(
                f"Something went wrong: {error}"
            )