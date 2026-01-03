from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic.hub import pull
from dotenv import load_dotenv
import requests
import os


load_dotenv()

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """
    url = f"https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}"

    response = requests.get(url=url)

    return response.json()


llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

## Step 2: Pull the ReAct prompt from Langchain hub
prompt = pull("hwchase17/react") # pulls the standard ReAct agent prompt





## Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool,get_weather_data],
    prompt=prompt
)


## Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool,get_weather_data],
    verbose=True
)

response = agent_executor.invoke({"input": "Find the capital of Telangana, Then find it's weather condition"})

print(response)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/16.AIAgent_using_Langchain (main)
# $ py 1_creating_simple_agent.py


# > Entering new AgentExecutor chain...
# I can search for the capital of Telangana and then use the weather data function to find the weather condition there.
# Action: duckduckgo_search
# Action Input: "capital of Telangana"1 day ago - It is the eleventh largest state by area and the twelfth most populated state in India, according to the 2011 census. On 2 June 2014, Telangana was separated from the northwestern part of United Andhra Pradesh as a newly formed state, with Hyderabad as its capital. 2 days ago - Hyderabad is the capital and largest city of the Indian state of Telangana. It occupies 650 km2 (250 sq mi) on the Deccan Plateau along the banks of the Musi River, in the northern part of Southern India. With an average altitude of 
# 536 m (1,759 ft), much of Hyderabad is situated on hilly terrain ... 1 month ago - On 2 June 2014, the state of Telangana was formed splitting from the rest of Andhra Pradesh state and formed the 29th state of India, with Hyderabad as its capital. November 15, 2025 - Hyderabad is the capital of the Indian state of Telangana. It is a historic city noted for its many monuments, temples, mosques and bazaars. A multitude of influences have shaped the character of the city in the last 400 years. The city of Hyderabad was founded by the Qutb Shahi sultan Muhammad ... 3 weeks ago - As per the Andhra Pradesh Reorganisation Act, 2014, Hyderabad became the capital of the newly formed state of Telangana, post bifurcation of Andhra Pradesh. The Central Government formed an expert committee to explore alternatives for the new ...I have found that the capital of Telangana is Hyderabad.
# Action: get_weather_data
# Action Input: Hyderabad{'request': {'type': 'City', 'query': 'Hyderabad, India', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Hyderabad', 'country': 'India', 'region': 'Telangana', 'lat': '17.375', 'lon': '78.474', 'timezone_id': 'Asia/Kolkata', 'localtime': '2026-01-03 
# 22:53', 'localtime_epoch': 1767480780, 'utc_offset': '5.50'}, 'current': {'observation_time': '05:23 PM', 'temperature': 21, 'weather_code': 143, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Mist'], 'astro': {'sunrise': '06:47 AM', 'sunset': '05:54 PM', 'moonrise': '05:53 PM', 'moonset': '06:36 AM', 'moon_phase': 'Full Moon', 'moon_illumination': 100}, 'air_quality': {'co': '527.85', 'no2': '11.75', 'o3': '137', 'so2': '10.45', 'pm2_5': '60.65', 'pm10': '61.65', 'us-epa-index': '3', 'gb-defra-index': '3'}, 'wind_speed': 17, 'wind_degree': 120, 'wind_dir': 'ESE', 'pressure': 1020, 'precip': 0, 'humidity': 78, 'cloudcover': 0, 'feelslike': 21, 'uv_index': 0, 'visibility': 3, 'is_day': 'no'}}I have retrieved the weather data for Hyderabad, which currently has a temperature of 21°C with misty weather.
# Final Answer: The capital of Telangana is Hyderabad, and the current weather condition there is misty with a temperature of 21°C.

# > Finished chain.
# {'input': "Find the capital of Telangana, Then find it's weather condition", 'output': 'The capital of Telangana is Hyderabad, and the current weather condition there is misty with a temperature of 21°C.'}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/16.AIAgent_using_Langchain (main)