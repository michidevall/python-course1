import requests


def get_weather_desc_and_temp():
    api_key = "95e05797624c1c72e3fd9b6a09ef8dd9"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

    request = requests.get(url)
    json = request.json()
    print(json)


    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'desription': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
   
def main():
     weather_dict = get_weather_desc_and_temp()
    #print the results

    print("Today's forcast is", weather_dict.get ('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

 main()