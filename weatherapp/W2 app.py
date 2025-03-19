# from ast import main
# import requests
# import time
# import datetime

# def get_smhi_weather(lat, lon):
#     url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{18.0215}/lat/{59.3099}/data.json"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         timeseries = data['timeSeries'][0]  
        
#         valid_time = timeseries['validTime']
#         time_formatted = datetime.datetime.strptime(valid_time, '%Y-%m-%dT%H:%M:%SZ' )
        
#         temperature = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 't')
#         wind_speed = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 'ws')
        
       
#         print(f'prognos för lördag 12 oktober 2024, 6:00-00:00')
#         print(f"Väderprognos för {time_formatted}:")
#         print(f"Temperatur: {temperature}°C")
#         print(f"Vindhastighet: {wind_speed} m/s")
#         print('-' * 30)
#     else:
#         print(f"Fel vid hämtning av väderdata. Statuskod: {response.status_code}")
    
# def menu():
#     print("Välkommen till väderapp!")
#     print("Välj en av följande alternativ:")
#     print("1. visa väder för ett dygn")
#     print("2. Hämta väderprognoser")
#     print("3. Avsluta")
    
# while True:
#     menu()
#     choice = input("Välj ett alternativ (1-3): ")

#     if choice == "1":
#         get_smhi_weather(59.30996552541549, 18.02151508449004 )
#     elif choice == "2":
#         get_smhi_weather(59.30996552541549, 18.02151508449004)    
#     elif choice == "3":
#         print("Avslutar applikationen")
#         exit()
#     else:
#         print("Ogiltig val. Välj 1, 2 eller 3")
#         menu()
#         time.sleep(1)  
        
#     if __name__ == "__main__":
#         main()
   

#.............................................................................................................................................


import requests
from datetime import datetime, timedelta
import pandas as pd


API_URL = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0215/lat/59.3099/data.json"

def main():
    print('Programmet startar...')  
    while True:
        print("\nMeny:")
        print("1. Hämta senaste väderdata från SMHI")
        print("2. Skriv ut senaste sparade prognos")
        print("9. Avsluta")
        val = input("Välj ett alternativ: ")

        if val == "1":
            get_weather_data()
        elif val == "2":
            print_weather_forecast()
        elif val == "9":
            print("Programmet avslutas.")
            break
        else:
            print("Felaktigt val, försök igen.")


def get_weather_data():
    print("Hämtar väderdata...")  
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        process_and_save_to_excel(data)
    else:
        print("Kunde inte hämta data från SMHI. Statuskod:", response.status_code)

# Funktion för att bearbeta och spara väderdata till Excel
def process_and_save_to_excel(data):
    forecasts = []
    current_time = datetime.now()
    tid_grans = current_time + timedelta(hours=24)  # Endast 24 timmars data

    for time_series in data['timeSeries']:
        date_time = time_series['validTime']
        forecast_time = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')  # Använd strptime för att konvertera
        
        if current_time <= forecast_time <= tid_grans:
            date = date_time.split('T')[0]  
            hour = forecast_time.hour  
            
            
            temp = next(param['values'][0] for param in time_series['parameters'] if param['name'] == 't')
            precipitation_category = next(param['values'][0] for param in time_series['parameters'] if param['name'] == 'pcat')
            rain_or_snow = precipitation_category in [1, 2]  

            forecasts.append({
                "Created": current_time,
                "Longitude": 18.02151508449004,
                "Latitude": 59.30996552541549,
                "Datum": date,
                "Hour": hour,
                "Temperature": temp,
                "RainOrSnow": rain_or_snow,
                "Provider": "SMHI"
            })

    
    if forecasts:  
        df = pd.DataFrame(forecasts)
        df.to_excel("weather_data.xlsx", index=False)
        print("Data sparad till 'weather_data.xlsx'.")
    else:
        print("Ingen väderdata för de närmaste 24 timmarna hittades.")


def print_weather_forecast():
    try:
        df = pd.read_excel("weather_data.xlsx")
        latest_date = df["Created"].max()  
        latest_data = df[df["Created"] == latest_date]  

        print(f"Prognos från SMHI {latest_date.date()}:")
        for index, row in latest_data.iterrows():
            precipitation = "Nederbörd" if row['RainOrSnow'] else "Ingen nederbörd"
            print(f"{row['Hour']:02d}:00 {row['Temperature']} grader {precipitation}")
    except FileNotFoundError:
        print("Ingen sparad data hittades.")
    except Exception as e:
        print("Ett fel inträffade:", e)


if __name__ == "__main__":
    main()











#..................................................................................................................................................................................................





# from requests_html import HTMLSession 
# s = HTMLSession()

# query = 'london'
# url = f'https://www.google.com/search?q=weather+{query}'

# r = s.get(url, headers = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15'})

# print(r.html.find('title'))




# #...................................................................................................................................................................................................................

# # exempel 1 på väder app

# import requests
# import datetime
# latitud = 59.30996552541549
# longitud = 18.02151508449004

# base_url = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{longitud}/lat/{latitud}/data.json'


# CityName = input('Enter City')
# completurl = base_url + CityName + 'appid=' + api_key

# response = requests.get(completurl)

# data = response.json()

# print(data)

# print('Nuvarande Temperature', data['main']['temp'])
# print('Nuvarande Temperature Feels like',data['main']['temp'])
# print('Maximal Temperature', data['main']['temp'])
# print('Minimum Temperature', data['main']['Celsius'])


# #.....................................................................................................................................................................................................................................................................
# # exempel 2
# from urllib import response
# from ast import main
# import requests
# import datetime
# latitud = 59.30996552541549
# longitud = 18.02151508449004

# def get_smhi_weather(lat, lon):
#     url = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{longitud}/lat/{latitud}/data.json'
#     response = requests.get()

#     if response.status_code == 200:
#         data = response.json()
#     timeseries = data['timeseries'][0]
#     valid_time = timeseries['validtime']
    
#     time = datetime.datetime.strptime(valid_time, '%Y-%m-%dT%H:%M:' )
    
#     temperature = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 'temperature') 
#     wind_speed = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 'wind_speed') 
    
#     print(f'väderprognos för {time}')
#     print(f'temperatures: {temperature} C ')
#     print(f'vindhastighet: {wind_speed} m/s')
 
# while True: 
#     print('Meny')
#     print('1:Hämta senaste prognosen')
#     print('2:skriva ut senaste prognosen')
#     print('3:Avsluta')
#     val = int(input('Ange ditt val 1-3'))
#     if val == 1:
#         data = get_smhi_weather()
#         print(data)
#     elif val == 2:
#         data = get_smhi_weather()
#         for prognos in data['data']:
#             print(f'Datum: {prognos["validFrom"]}, Varningstyp: {prognos["type"]}, Varningstext: {prognos["text"]}')
        
#     elif val == 3:
#         break
#     else:
#         print('Datum: {prognos["validFrom"]}, Varningst')
        
#     print('programmet avslutades') 
    
   
# latitud = 59.30996552541549
# longitud = 18.02151508449004

# get_smhi_weather(latitud, longitud)


# if __name__ == "__main__":
#     main()
   

# #.................................................................................................................................................................
