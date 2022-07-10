import requests
from twilio.rest import Client

api_key = "***************************"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

latitude = 49.012230
longitude = 14.505340

account_sid = "******************************"
auth_token = "*********************************"

weather_params = {
	"lat": latitude,
	"lon": longitude,
	"appid": api_key,
	"exclude": "current,minutely,daily"

}


response = requests.get(OWM_endpoint, params=weather_params)

response.raise_for_status()
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_slice:
	condition_code = hour_data["weather"][0]["id"]
	if int(condition_code) < 700:
		will_rain = True

if will_rain:
	client = Client(account_sid, auth_token)

	message = client.messages \
		.create(
		body="It's Going rain today bring umbrella !!!",
		from_='+19382382901',
		to='+420605026890')

	print(message.status)
