import requests, csv


APIKEY = ""
OUTPUTCSV = "temperature.csv"

def main():
    if APIKEY != "":
        cities = ["London","Austin","Paris","Jakarta"]
        location = []
        weatherDescript = []
        feelsLikeTemp = []
        huimidity = []
        ptr = 0
        for x in cities:
            #gets latitude and longitude
            geoCodeUrl = f'http://api.openweathermap.org/geo/1.0/direct?q={x}&appid={APIKEY}'
            response = requests.get(geoCodeUrl)
            geocodeData = response.json()
            location.append((geocodeData[0]["lat"],geocodeData[0]["lon"]))
            #gets the weather
            getWeatherUrl = f'https://api.openweathermap.org/data/2.5/weather?lat={location[ptr][0]}&lon={location[ptr][1]}&appid={APIKEY}&units=metric'
            response = requests.get(getWeatherUrl)
            weatherData = response.json()
            weatherDescript.append(weatherData["weather"][0]["description"])
            feelsLikeTemp.append(weatherData["main"]["feels_like"])
            huimidity.append(weatherData["main"]["humidity"])
            ptr += 1

        finalRows = [["city","Feels Like","Humidity"]]

        for x in range(len(cities)):
            finalRows.append([cities[x],str(feelsLikeTemp[x])+"C",str(huimidity[x])+"%"])


        with open(OUTPUTCSV,'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerows(finalRows)

        print("done!")
    else:
        print("API key not entered")

main()
