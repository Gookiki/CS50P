def checks():
    fraction = input("Fraction: ")
    x, y = fraction.split("/")

    if x.isdigit() and y.isdigit() and int(y) >= int(x) and int(y) != 0:
        result = round(int(x) / int(y) * 100)
        if result <= 1:
            return "E"
        elif result >= 99:
            return "F"
        else:
            percent = f"{round(int(x) / int(y) * 100)}%"
            return(percent)
    else:
        return False
    
