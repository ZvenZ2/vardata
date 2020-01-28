from datafiler.create_directory import create_directory
from datafiler.download_data import download_data
from datafiler.dict_all_weather_data import get_dict_data
from datafiler.write_to_xlsx import write_to_excel
from datafiler.check_heat_turn_on import turn_on_heat
from datafiler.deletes_file import remove



def main_program(hours_ahead):
        # Laster ned værdata og legger det inn i XML-fil under 'datafiles'
        # Data som skal lastes nes kan spesifiseres, ved å skrive inn gitt url
        # Ingen verdi satt inn gir ski - "https://www.yr.no/sted/Norge/Akershus/Ski/Ski/varsel_time_for_time.xml"
        # Lagres på en xml-fil, "weather_data.xml"
    download_data()

        # Henter ut all informasjon er er brukbar i xml-filen i en dictionary
        # Fil informasjonen skal entes fra kan spesifiseres, xml-fil må da liggge i samme mappe som main fil
    data = get_dict_data()

        # Sletter xml-filen til værdataet ettersom at all informasjon er hentet ut
        # Fil som skal slettes kan spesistiseres, hvis ingen ting er gitt, så slettes filen "weather_data.xml"
    remove()

        # Kjører funksjon som lager mappen excel om det ikke alerede finnes
        # Mappe som lages kan spesisifiseres, men hvis ingen ting er gitt, så lages mappen excel
    create_directory()

        # Skriver værverdier inn i excel
    write_to_excel(data)

        # Skjekker om varme burde skrus på
    turn_on_heat(data, hours_ahead)
        #sleep_time = sleep_time*60

