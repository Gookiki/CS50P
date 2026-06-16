def main():
    groceries = {}

    while True:
        try:
            groceryitem = input().strip().lower()
        except EOFError:
            break

        if groceryitem == "":
            continue

        groceries[groceryitem] = groceries.get(groceryitem, 0) + 1

    for item in sorted(groceries):
        print(groceries[item], item.upper())


if __name__ == "__main__":
    main()
