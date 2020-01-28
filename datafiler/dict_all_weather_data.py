import xml.etree.ElementTree as ET
# Finner all nyttig værdata i XML-filen og legger det til i en dict

# Dict med alle betydinger av tallene numberEx
# {1: 'Klarvær', 2: 'Lettskyet', 3: 'Delvis skyet', 4: 'Skyet', 5: 'Regn byger', 6: 'Regnbyger med torden', 7: 'Sluddbyger', 8: 'Snøbyger', 9: 'Regn', 10: 'Kraftig regn', 11: 'Kraftig regn og torden', 12: 'Sludd', 13: 'Snø', 14: 'Snø og torden', 15: 'Tåke', 16: '#', 17: '#', 18: '#', 19: '#', 20: 'Sluddbyger og torden', 21: 'Snøbyger og torden', 22: 'Regn og torden', 23: 'Sludd og torden', 24: 'Lette regnbyger og torden', 25: 'Kraftige regnbyger og torden', 26: 'Lette sluddbyger og torden', 27: 'Kraftige sluddbyger og torden', 28: 'Lette snøbyger og torden', 29: 'Kraftige snøbyger og torden', 30: 'Lett regn og torden', 31: 'Lett sludd og torden', 32: 'Kraftig sludd og torden', 33: 'Lett snø og torden', 34: 'Kraftig snø og torden', 35: '#', 36: '#', 37: '#', 38: '#', 39: '#', 40: 'Lette regnbyger', 41: 'Kraftige regnbyger', 42: 'Lette sluddbyger', 43: 'Kraftige sluddbyger', 44: 'Lette snøbyger', 45: 'Kraftige snøbyger', 46: 'Lett regn', 47: 'Lett sludd', 48: 'Kraftig sludd', 49: 'Lett snø', 50: 'Kraftig snø'}

def get_dict_data(file = str("weather_data.xml")):
    print("# retrieves information from xml")
    # Åpner files som skal leses
    data = ET.parse(file)
    root = data.getroot()

    # Lager en dict hvor alle verdiene skal ligge
    data_dict = {}

    # Legger til områdeverdier i data_dict
    data_dict["area"] = [str(root[0][0].text), str(root[0][2].text)]

    # Legger til forrige og neste update
    update = {}
    update["last"] = str(root[3][0].text)
    update["next"] = str(root[3][1].text)
    data_dict["update"] = update

    # Legger til soloppgang og solnedgang
    dict_sol = root[4].attrib
    data_dict["sun"] = dict_sol

    # Legger til alle værdata
    vardata = root[5][1]
    verdier = vardata[0]
    i = 1
    dict_all_weather_data = {}
    for verdier in vardata:
        mellom_dict = {}

        # Legger til start og slutt tid
        time = verdier.attrib
        dict_time = {}
        dict_time["start"] = time["from"]
        dict_time["end"] = time["to"]
        mellom_dict["time"] = dict_time

        # Legger til kode av hvordan været er
        dict_weather = {}
        dict_weather["code"] = verdier[0].attrib["numberEx"]
        dict_weather["name"] = verdier[0].attrib["name"]
        mellom_dict["weather"] = dict_weather

        # Legger til nedbørsmengde
        rainfall = verdier[1].attrib
        dict_rainfall = {}
        dict_rainfall["expected"] = rainfall["value"]
        if not("minvalue" in rainfall):
            dict_rainfall["min"] = rainfall["value"]
        else:
            dict_rainfall["min"] = rainfall["minvalue"]
        if not("minvalue" in rainfall):
            dict_rainfall["max"] = rainfall["value"]
        else:
            dict_rainfall["max"] = rainfall["maxvalue"]
        mellom_dict["rainfall"] = dict_rainfall

        # Legger til vindretning
        wind_direction = verdier[2].attrib
        dict_wind_direction = {}
        dict_wind_direction["direction"] = wind_direction["deg"]
        dict_wind_direction["name"] = wind_direction["name"]
        mellom_dict["wind_direction"] = dict_wind_direction

        # Legger til vindhastighet
        dict_wind_speed = verdier[3].attrib
        mellom_dict["wind_speed"] = dict_wind_speed

        # Legger til temperatur (Oppgis i Celsius)
        mellom_dict["temprature"] = verdier[4].attrib["value"]

        # Legger til trykk (Oppgis i hPa)
        mellom_dict["pressure"] = verdier[5].attrib["value"]
        dict_all_weather_data[i] = mellom_dict
        i += 1

    last_dictionary = {}
    last_dictionary["basic_info"] = data_dict
    last_dictionary["weather"] = dict_all_weather_data

    print("# information from xml obtained")
    return last_dictionary

