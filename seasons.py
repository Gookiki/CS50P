# seasons.py
from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def minutes_as_words(date_str: str) -> str:
    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date")

    today = date.today()
    if birthdate > today:
        raise ValueError("Invalid date")

    minutes = round((today - birthdate).total_seconds() / 60)
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"

def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ").strip()
    try:
        print(minutes_as_words(birth_str))
    except ValueError:
        print("Invalid date")
        sys.exit(1)

if __name__ == "__main__":
    main()
