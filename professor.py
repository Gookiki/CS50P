import random


def get_level():
    while True:
        try:
            level = int(input("Level (1-3): "))
        except ValueError:
            continue
        except EOFError:
            return None

        if level in [1, 2, 3]:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    return random.randint(100, 999)


def main():
    level = get_level()
    if level is None:
        return

    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        for tries in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if tries == 2:
                    print("CORRECT ANSWER:", correct)
                continue

            if answer == correct:
                score += 1
                break

            print("EEE")
            if tries == 2:
                print("CORRECT ANSWER:", correct)

    print("Score:", score)


if __name__ == "__main__":
    main()
