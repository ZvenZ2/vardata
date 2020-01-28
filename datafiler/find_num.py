def find_num(setning, min, max):
    hours_ahead = input(str(setning))
    if hours_ahead == "":
        return hours_ahead

    try:
        num = int(hours_ahead)
        if (num >= int(min)) and (num <= int(max)):
            num = int(num)
        else:
            print(f"Gi ett tall mellom {min} og {max}")
            num = find_num(setning, min, max)
    except:
        print(f"Gi ett tall mellom {min} og {max}")
        num = find_num(setning, min, max)
    finally:
        return num