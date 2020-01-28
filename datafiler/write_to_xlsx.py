import xlsxwriter


def write_to_excel(weather_values):
    data = weather_values
    print("# creating xlsx-file")
    # Lager excel-fil og regneark som brukes i mappe
    try:
        outWorkbook = xlsxwriter.Workbook("excel/data.xlsx")
        sheet = outWorkbook.add_worksheet("Weather Data")

        # Skriver først inn informasjonen som bare nevnes en gang
        long_term_info = data["basic_info"]

        print("# writing to xlsx")
        sheet.write(0,0, "BASIC INFO")

        # Skriver inn område
        town = long_term_info["area"][0]
        country = long_term_info["area"][1]
        area = str(f"{town}, {country}")
        sheet.write(2, 0, "Area:")
        sheet.write(2, 1, area)

        # Skriver inn uppdateringstid
        sheet.write(3, 0, "Last update:")
        sheet.write(4, 0, "Next update:")
        last_update = long_term_info["update"]["last"]
        next_update = long_term_info["update"]["next"]
        last_update = last_update.replace("T", " | ")
        next_update = next_update.replace("T", " | ")
        sheet.write(3, 1, last_update)
        sheet.write(4, 1, next_update)

        # Skriver inn soloppgang og solnedgang
        sheet.write(5,0, "Sunrise:")
        sheet.write(6, 0, "Sunset:")
        sun_rise = long_term_info["sun"]["rise"]
        sun_set = long_term_info["sun"]["set"]
        sun_rise = sun_rise.replace("T", " | ")
        sun_set = sun_set.replace("T", " | ")
        sheet.write(5, 1, sun_rise)
        sheet.write(6, 1, sun_set)


        # Skriver inn alle overskriftene til timesdataene
        sheet.write(0, 3, "Weather Data")
        sheet.write(2, 3, "Time (1 hour)")
        sheet.write(2, 4, "Weather")
        sheet.write(2, 5, "Rainfall (mm)")
        sheet.write(2, 7, "Wind Direction")
        sheet.write(2, 8, "Wind Speed (mps)")
        sheet.write(2, 10, "Temprature (°C)")
        sheet.write(2, 11, "Air Pressure (hPa)")

        # Skriver inn alle værverdier
        weather_data = data["weather"]

        for i in weather_data:
            line = (int(i)) + 2
            data_now = weather_data[i]

            # Skriver inn start og slutttid
            start = data_now["time"]["start"]
            start = start.replace("T", " | ")
            sheet.write(line, 3, start)

            # Skriver inn hvordan været er
            weather = data_now["weather"]["name"]
            sheet.write(line, 4, weather)

            # Skriver inn nedbørsmengde
            rainfall = data_now["rainfall"]
            expected = float(rainfall["expected"])
            min = float(rainfall["min"])
            max = float(rainfall["max"])
            plus = str((max*10-expected*10)/10)
            minus = str((expected*10-min*10)/10)
            deviation = str("+" + str(plus) + "/-" + str(minus))
            sheet.write(line, 5, expected)
            sheet.write(line, 6, deviation)

            # Skriver inn vindretning
            wind_direction = data_now["wind_direction"]
            wind_deg = wind_direction["direction"]
            wind_deg_name = wind_direction["name"]
            wind_dir = wind_deg + "° " + wind_deg_name
            sheet.write(line, 7, wind_dir)

            # Skriver inn vindhastighet
            wind_speed = data_now["wind_speed"]
            wind_speed_mps = float(wind_speed["mps"])
            wind_speed_name = wind_speed["name"]
            wind_sp_name = "- " + wind_speed_name
            sheet.write(line, 8, wind_speed_mps)
            sheet.write(line, 9, wind_sp_name)

            # Skriver inn tempraturen
            temrature = float(data_now["temprature"])
            sheet.write(line, 10, temrature)

            # Skriver inn lufttrykket
            pressure = float(data_now["pressure"])
            sheet.write(line, 11, pressure)

        # Setter bredde på excel rutenett
        sheet.set_column(0, 0, 17)
        sheet.set_column(1, 1, 20)
        sheet.set_column(3, 3, 20)
        sheet.set_column(4, 4, 12)
        sheet. set_column(5, 5, 14)
        sheet.set_column(6, 6, 8)
        sheet.set_column(7, 7, 20)
        sheet.set_column(8, 8, 18)
        sheet.set_column(9, 9, 20)
        sheet.set_column(10, 10, 16)
        sheet.set_column(11, 11, 17)

        # Lukker den ferdige excel-filen
        outWorkbook.close()
        print("# written to xlsx-file")
    # Hvis det oppstår error under slriving, mest sansynelig at fil ikke er lukket
    except:
        print("Error: failed to write to XLSX-file, check that file is closed.")

