from os import remove as rm

# Kort funksjon som fjerner filer
def remove(file = "weather_data.xml"):
    file = file
    print(f"# Removing {str(file)}")
    rm(file)