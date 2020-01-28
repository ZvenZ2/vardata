from urllib import request as ur
from sys import exit

# Funksjon som laster ned værdata med mulighet til å legge inn egen URL hvis område ønsket ikke er Ski
def download_data(url = "https://www.yr.no/sted/Norge/Akershus/Ski/Ski/varsel_time_for_time.xml", name = "weather_data.xml"):
    # Laster ned XML-fil av værdata fra yr
    try:
        page = ur.urlopen(str(url))
        data = page.read()
        print("# weather data downloaded")
    except:
        print("Error: weather data not found")
        exit()

    # Lager en tom XML-fil sog legger inn all værdata fra yt i XML-filen under mappen 'datafiles'
    try:
        directory = name
        datafil = open(directory, "wb")
        datafil.write(data)
        datafil.close()
        print(f"# weather data written to '{directory}'")
    except:
        print(f"Error: wather data could could not be written to '{directory}'")
        exit()
