import xml.etree.ElementTree as ET
from datafiler.find_num import find_num


# Funksjon som skriver settings til xml-fil om det ikke alerede er gitt
def write_setings():
    delay = find_num("Hvor ofte skal programmet kjøre, i sekunder? ", 1, 1000000)
    hours_ahead = find_num("Hvor mange timer fremover skal skjekkes? ", 1, 48)

    root = ET.Element("root")
    ET.SubElement(root, "timer_fremover").text = str(hours_ahead)
    ET.SubElement(root, "delay").text = str(delay)
    tree = ET.ElementTree(root)

    tree.write("./settings.xml", encoding='utf-8', xml_declaration=True)

# Funksjon som skjekker om det alerede eksisterer settings, hvis ikke hentes settings fra bruker
def get_settings():
    # Prøver å hente data fra settings
    try:
        data = ET.parse("./settings.xml")
        root = data.getroot()
        data = {}
        for element in root:
            if element.tag == "timer_fremover":
                data["timer_fremover"] = int(element.text)
            elif element.tag == "delay":
                data["delay"] = int(element.text)
            else:
                raise Exception("Feil i setings fil, element eksisterer ikke.")
        return data
    # Lager en fil med settings hvis det ikke finnes, eller det ppstår en feil
    except:
        write_setings()
        data = get_settings()
    finally:
        return data

