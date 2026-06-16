def convert(fraction):
    try:
        x, y = fraction.split("/")
    except ValueError:
        raise ValueError

    if not x.isdigit() or not y.isdigit():
        raise ValueError

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


def checks(fraction):
    try:
        percentage = convert(fraction)
        return gauge(percentage)
    except (ValueError, ZeroDivisionError):
        return False


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
