import requests
from datetime import datetime, timedelta
import pandas as pd
 
# API URL för väderprognos från SMHI för Liljeholmen
API_URL = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02151508449004/lat/59.30996552541549/data.json"
 
def main():
    print('biiiitch')
    while True:
        print("\nMeny:")
        print("1. Hämta senaste väderdata från SMHI")
        print("2. Skriv ut senaste sparade prognos")
        print("3. Avsluta")
        val = input("Välj ett alternativ: ")
        
        if val == "1":
            get_weather_data()
        elif val == "2":
            print_weather_forecast()
        elif val == "3":
            print("Programmet avslutas.")
            break
        else:
            print("Felaktigt val, försök igen.")
 
# Funktion för att hämta och bearbeta väderdata från SMHI
def get_weather_data():
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
        forecast_time = datetime.fromisoformat(date_time[:-1])
        
        # Kontrollera att datumet är inom de närmaste 24 timmarna
        if current_time <= forecast_time <= tid_grans:
            date = date_time.split('T')[0]  # Datumdel
            hour = int(date_time.split('T')[1][:2])  # Timme
            
            # Temperatur och nederbörd
            temp = next(param['values'][0] for param in time_series['parameters'] if param['name'] == 't')
            precipitation_category = next(param['values'][0] for param in time_series['parameters'] if param['name'] == 'pcat')
            rain_or_snow = precipitation_category in [1, 2]  # 1 och 2 är regn eller snö
            
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
    
    # Skapa en DataFrame och spara till Excel
    df = pd.DataFrame(forecasts)
    df.to_excel("weather_data.xlsx", index=False)
    print("Data sparad till 'weather_data.xlsx'.")
 
# Funktion för att skriva ut väderprognos från Excel-filen
def print_weather_forecast():
    try:
        df = pd.read_excel("weather_data.xlsx")
        latest_date = df["Created"].max()  # Hämta senaste sparade datum
        latest_data = df[df["Created"] == latest_date]  # Filtrera data för senaste prognosen
        
        print(f"Prognos från SMHI {latest_date.date()}:")
        for index, row in latest_data.iterrows():
            precipitation = "Nederbörd" if row['RainOrSnow'] else "Ingen nederbörd"
            print(f"{row['Hour']:02d}:00 {row['Temperature']} grader {precipitation}")
    except FileNotFoundError:
        print("Ingen sparad data hittades.")
 
# Kör programmet
if __name__ == "__main__":
    main()
 