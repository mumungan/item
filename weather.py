import requests
import json

city = "jeju" #도시
lat = 33.3
lon = 126.4
apiKey = "4379ff2314852e2e97702484afee10a9"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

print(result)