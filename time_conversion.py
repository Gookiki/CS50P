def main():
    time = input("What is the current time? ")
    value = convert(time)

    if 7 <= value <= 8:
        print("Breakfast")
    elif 12 <= value <= 13:
        print("Lunch")
    elif 18 <= value <= 19:
        print("Dinner")
    else:
        print("Nothing")


def convert(time):
    s = time.strip()
    ampm = ""

    if len(s) > 2 and s[-2:].lower() in ("am", "pm"):
        ampm = s[-2:].lower()
        s = s[:-2].strip()

    hours_str, minutes_str = s.split(":")
    hours = int(hours_str)
    minutes = int(minutes_str) / 60

    if ampm == "pm" and hours != 12:
        hours += 12
    if ampm == "am" and hours == 12:
        hours = 0

    return hours + minutes


if __name__ == "__main__":
    main()
