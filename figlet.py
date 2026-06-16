import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    args = sys.argv[1:]

    if len(args) == 0:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    elif len(args) == 2:
        if args[0] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        font = args[1]
        if font not in figlet.getFonts():
            sys.exit("Invalid usage")
        figlet.setFont(font=font)
    else:
        sys.exit("Invalid usage")

    text = input()
    print(figlet.renderText(text), end="")


if __name__ == "__main__":
    main()
