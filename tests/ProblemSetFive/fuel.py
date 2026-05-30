
    
def checks(fraction: str | None = None):
    """Return fuel percentage string for a fraction like '1/2'.
    If fraction is None, prompt the user (preserve interactive behavior).
    Returns 'E' or 'F' for near-empty/full, or False for invalid input.
    """
    if fraction is None:
        fraction = input("Fraction: ")

    # Basic format validation: must contain exactly one '/'
    if fraction.count("/") != 1:
        return False

    x_str, y_str = fraction.split("/")

    # Ensure both parts are integers
    if not (x_str.isdigit() and y_str.isdigit()):
        return False

    x = int(x_str)
    y = int(y_str)

    # Denominator must be non-zero and numerator must not exceed denominator
    if y == 0 or x > y:
        return False

    percent = round(x / y * 100)

    if percent <= 1:
        return "E"
    if percent >= 99:
        return "F"
    return f"{percent}%"
    
