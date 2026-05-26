def main():
    inputword = input("Enter a word: ")
    print(shorten(inputword))

def shorten(word):
    newword = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            newword += letter
    return newword

if __name__ == "__main__":
    main()