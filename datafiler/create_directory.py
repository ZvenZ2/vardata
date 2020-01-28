from os import mkdir, path

def create_directory(folder = "excel"):
    print("# creating directory path")
    # Mappe som skal skjekkes om finnes, hvis ikke, så lages mappen
    directory = str(folder)
    if not(path.exists(directory)):

        try:
            mkdir(directory)
        except OSError:
            print(f"# creation of the directory {directory} failed")
        else:
            print(f"# created the directory {directory}")

    else:
        print(f"# directory '{directory}' already exist")
