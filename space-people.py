import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

for person in json['people']:
    print(person['name'])




api_key = "95e05797624c1c72e3fd9b6a09ef8dd9"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

request = requests.get(url)
json = request.json()
print(json)