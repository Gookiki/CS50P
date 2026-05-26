import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        # Return a boolean. re.match returns a Match object or None; wrap with bool()
        return 2 <= len(s) <= 6 and s[:2].isalpha() and bool(re.match(r"[a-zA-Z]{2,}([1-9]\d*)?$", s))

   
if __name__ == "__main__":
    main()