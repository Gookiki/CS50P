from pyfiglet import Figlet, FontNotFound
import sys
import argparse

p = argparse.ArgumentParser()
# Make -f/--font optional and default to "standard"
p.add_argument("-f", "--font", help = "Font to use for output", default="standard")
args = p.parse_args()

# Pass the font into figlet_format
try:
    f = Figlet(font=args.font)
except FontNotFound:
    print("Font not found.")
    sys.exit(1)
sentence = input("Sentence: ")
print("Output: ", end="")
print(f.renderText(sentence))