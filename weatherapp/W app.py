
# from ast import main
# import requests
# import time
# import datetime
# import pandas as pd
# import openpyxl 



# EXEL_FILE = 'weather.xlsx'

# def get_smhi_weather(lat, lon):
#     url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{18.0215}/lat/{59.3099}/data.json"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         timeseries = data['timeSeries'][0]  
#         weather_data =[]
        
#         for timseeries in data['timeSeries']:
#         valid_time = timeseries['validTime']
#         time_formatted = datetime.datetime.strptime(valid_time, '%Y-%m-%dT%H:%M:%SZ' )
        
        
        
        
#         temperature = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 't')
#         wind_speed = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 'ws')
#         return weather_data
#     else:
#         print(f'fel vid hämtning av data {response.status_code}')
    
        
        
#         print(f'prognos för lördag 12 oktober 2024, 6:00-00:00')
#         print(f"Väderprognos för {time_formatted}:")
#         print(f"Temperatur: {temperature}°C")
#         print(f"Vindhastighet: {wind_speed} m/s")
#         print('-' * 30)
#     else:
#         print(f"Fel vid hämtning av väderdata. Statuskod: {response.status_code}")
        

#     df = pd.DataFrame()
#     df.to_excel(EXEL_FILE, index=False) 
#     print('Data hämtas och sparas i EXEL_FILE (weather.xlsx')
    



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
#         get_smhi_weather(59.30996552541549, 18.02151508449004)
#     elif choice == "2":
#         get_smhi_weather(59.30996552541549, 18.02151508449004)    
#     elif choice == "3":
#         print("Avslutar applikationen")
#         exit()
#     else:
#         print("Ogiltig val. Välj 1, 2 eller 3")
#         menu()
#         time.sleep(1)  
      
      
#     def save_weather_to_excel(weather_data, filname= 'smhi_weatherxlsx'):
#         """sparar väderdata till en excel-fil.""" 
#         df = pd:dataframe(weather_data)
        
    
        
#     print(f'väderdata har sparats till{filename}')   
        
        
#     if __name__ == "__main__":
#         main()
  
  
  
   


#.....................................................................................................................................................................................




# import requests
# import datetime
# latitud = 59.30996552541549
# longitud = 18.02151508449004

# def get_weather(lat, lon):
#     base_url = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{18.0215}/lat/{59.3099}/data.json'
#     response = requests.get(base_url)
    
#     if response.status_code == 200:
#         weather_data = response.json()
#         return weather_data 
#     else:
#         print(f'erorr {response.status_code}')
#         return None
    
# lat, lon = 59.3099, 18.0215
# weather_data = get_weather(lat, lon)

# if weather_data:
#     print('väderdata hämtad framgångsrikt')







#..............................................................................................................................................................................





# import requests
# import datetime
# latitud = 59.30996552541549
# longitud = 18.02151508449004

# def get_weather(lat, lon):
#     base_url = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{18.0215}/lat/{59.3099}/data.json'
#     response = requests.get(base_url)
    
#     if response.status_code == 200:
#         weather_data = response.json()
#         return weather_data 
#     else:
#         print(f'erorr {response.status_code}')
#         return None

# def hämta_data():
#     datum = datetime.datetime.fromtimestamp(datetime.timedelta)
#     response = requests.get(base_url)
#     if response.status_code == 200:
#         data = response.json()
#         print('Nuvarande Temperature', data['main']['temp'])
#         print('Maximal Temperature', data['main']['temp'])
#         print('Minimum Temperature', data['main']['Celsius'])
#         return data
#     else:
#         print(f'fel hämtade data: status code {response.status_code}')

# while True: 
#     print('Meny')
#     print('1:Hämta senaste prognosen')
#     print('2:skriva ut senaste prognosen')
#     print('3:Avsluta')
#     val = int(input('Ange ditt val 1-3'))
#     if val == 1:
#         data = hämta_data()
#         print(data)
#     elif val == 2:
#         data = hämta_data()
#         for prognos in data['data']:
#             print(f'Datum: {prognos["validFrom"]}, Varningstyp: {prognos["type"]}, Varningstext: {prognos["text"]}')
        
#     elif val == 3:
#         break
#     else:
#         print('Datum: {prognos["validFrom"]}, Varningst')
        
#     print('programmet avslutades')


#...................................................................................................................................................................................


    
# import requests
# import pandas as pd
# import datetime

# def get_smhi_weather_for_day(lat, lon):
#     """Hämtar väderprognoser för ett helt dygn och returnerar en lista med data."""
#     url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         time_now = datetime.datetime.utcnow()
        
#         weather_data = []
        
#         # Loopa genom alla tidserier och samla data för kommande 24 timmar
#         for timeseries in data['timeSeries']:
#             valid_time = timeseries['validTime']
#             time_formatted = datetime.datetime.strptime(valid_time, '%Y-%m-%dT%H:%M:%SZ')

#             if time_formatted > time_now and time_formatted < (time_now + datetime.timedelta(days=1)):
#                 temperature = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 't')
#                 wind_speed = next(param['values'][0] for param in timeseries['parameters'] if param['name'] == 'ws')
                
#                 weather_data.append({
#                     'Datum och tid': time_formatted.strftime('%Y-%m-%d %H:%M'),
#                     'Temperatur (°C)': temperature,
#                     'Vindhastighet (m/s)': wind_speed
#                 })
#         return weather_data
#     else:
#         print(f"Fel vid hämtning av väderdata. Statuskod: {response.status_code}")
#         return []

# def save_weather_to_excel(weather_data, filename='smhi_weather.xlsx'):
#     """Sparar väderdata till en Excel-fil."""
#     df = pd.DataFrame(weather_data)
    
#     # Spara till Excel-fil
#     with pd.ExcelWriter(filename, engine='openpyxl', mode='w') as writer:
#         df.to_excel(writer, index=False, sheet_name='Väderprognos')

#     print(f"Väderdata har sparats till {filename}")

# def main():
#     latitude = 59.3293  # Stockholm latitud (justera om du vill)
#     longitude = 18.0686  # Stockholm longitud (justera om du vill)

#     # Hämta väderdata för ett helt dygn
#     weather_data = get_smhi_weather_for_day(latitude, longitude)
    
#     if weather_data:
#         # Spara väderdata till en Excel-fil
#         save_weather_to_excel(weather_data)

# if __name__ == "__main__":
#     main()

#.....................................................................................................................................................




