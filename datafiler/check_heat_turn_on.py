
# Kunksjon som skjekker om varme burde skrus på
def turn_on_heat(data, hours_ahead):
    dict_all_weather_values = {1: 'Klarvær', 2: 'Lettskyet', 3: 'Delvis skyet', 4: 'Skyet', 5: 'Regn byger', 6: 'Regnbyger med torden', 7: 'Sluddbyger', 8: 'Snøbyger', 9: 'Regn', 10: 'Kraftig regn', 11: 'Kraftig regn og torden', 12: 'Sludd', 13: 'Snø', 14: 'Snø og torden', 15: 'Tåke', 16: '#', 17: '#', 18: '#', 19: '#', 20: 'Sluddbyger og torden', 21: 'Snøbyger og torden', 22: 'Regn og torden', 23: 'Sludd og torden', 24: 'Lette regnbyger og torden', 25: 'Kraftige regnbyger og torden', 26: 'Lette sluddbyger og torden', 27: 'Kraftige sluddbyger og torden', 28: 'Lette snøbyger og torden', 29: 'Kraftige snøbyger og torden', 30: 'Lett regn og torden', 31: 'Lett sludd og torden', 32: 'Kraftig sludd og torden', 33: 'Lett snø og torden', 34: 'Kraftig snø og torden', 35: '#', 36: '#', 37: '#', 38: '#', 39: '#', 40: 'Lette regnbyger', 41: 'Kraftige regnbyger', 42: 'Lette sluddbyger', 43: 'Kraftige sluddbyger', 44: 'Lette snøbyger', 45: 'Kraftige snøbyger', 46: 'Lett regn', 47: 'Lett sludd', 48: 'Kraftig sludd', 49: 'Lett snø', 50: 'Kraftig snø'}
    data = data
    if hours_ahead == "":
        hours_ahead = 10
    else:
        hours_ahead = int(hours_ahead)

    print("# checks if heat should be turned on")

    num = 1
    weather_values = {}
    temp_values = {}
    # Legger til alle koder av hvordan været er ventet fremover, og hva tempraturen er ventet fremover
    while num <= hours_ahead:
        weather_values[int(num)] = int(data["weather"][int(num)]["weather"]["code"])
        temp_values[int(num)] = int(data["weather"][int(num)]["temprature"])
        num+=1

    # Funksjon for skjekker om varme burde skrus på basert på været
    def heat_weather(values):
        # Liste med verdier som medsier et varmen skal skrus på
        list_impact_values = [8, 13, 14, 21, 28, 29, 33, 34, 44, 45, 49, 50]
        list_impact_values_found = {}
        for i in values:
            if values[i] in list_impact_values:
                list_impact_values_found[i] = values[i]
        return list_impact_values_found

    def wet_cold_weather(values, temp):
        # Liste med verdier som medsier at været er vått, sludd og regn
        list_impact_values = [5, 6, 7, 9, 10, 11, 20, 23, 24, 25, 26, 27, 30, 31, 32, 33, 40, 41, 42, 43, 46, 47, 48]
        list_impact_times = []
        for i in values:
            if values[i] in list_impact_values:
                list_impact_times.append(i)
        temp_values_under_zero = {}
        # Skjekker videre
        if len(list_impact_times) > 0:
            list_times_to_check = range(int(list_impact_times[0]), int(hours_ahead)+1)
            for i in list_times_to_check:
                if int(temp[i]) <= 0:
                    temp_values_under_zero[i] = int(temp[i])
            if len(temp_values_under_zero) > 0:
                return_dict = {}
                return_dict["reason"] = values[int(list_impact_times[0])]
                return_dict["om"] = int(list_impact_times[0])
                return_dict["values"] = temp_values_under_zero
                # Hvis det er ventet fuktig vær, og minusgrader samtidig eller like etter, så returneres en dict med info om dette
                return return_dict
            else:
                return {}
        else:
            return {}

        # Returnerer verdier som er under 0 grader etter at ett av utfallene, og verdi



    by_weather = heat_weather(weather_values)
    temp = wet_cold_weather(weather_values, temp_values)
    print("---")
    print("---")
    print("---")

    # Printer alle værverdier som er reeele
    if (len(by_weather) > 0) or (len(temp) > 0):
        print(f"Været ventet innen {hours_ahead} timer fremover forutsier at varme burde skrus på:")
        if (len(by_weather) > 0):
            print("Ventet:")
            for i in by_weather:
                if i == 1:
                    print(f"- {dict_all_weather_values[int(by_weather[i])]} innen {i} time.")
                else:
                    print(f"- {dict_all_weather_values[int(by_weather[i])]} innen {i} timer.")
        if len(temp) > 0:
            reason = dict_all_weather_values[int(temp["reason"])]
            om = temp["om"]
            values = temp["values"]
            print(f"Det er ventet {reason} innen {om} timer, og:")
            for i in values:
                print(f"{values[i]}°C innen {i} timer")

    else:
        print(f"Været ventet innen {hours_ahead} timer fremover forutsier at varme ikke trengs å skrus på.")