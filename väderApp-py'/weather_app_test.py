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


def process_and_save_to_excel(data):
    forecasts = []
    current_time = datetime.now()
    tid_grans = current_time + timedelta(hours=24)  

    for time_series in data['timeSeries']:
        date_time = time_series['validTime']
        forecast_time = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')  
        
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
