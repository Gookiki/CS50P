def main():
    greet = input("Greeting: ")
    print(f"${value(greet)}")


def value(greeting):
    if greeting.lower().startswith("hello"):
        return 100
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()