import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            if sys.stdin.isatty():
                name = input("Name: ")
            else:
                name = input()
        except EOFError:
            break

        names.append(name)

    if names:
        print("Adieu, adieu, to", p.join(names))

if __name__ == "__main__":
    main()