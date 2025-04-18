import random


def roll_dice():
    die1, die2 = random.randint(1, 6), random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2} → Total: {die1 + die2}")


def main():
    die1 = 10
    print(f"die1 in main() starts as: {die1}")

    for _ in range(3):
        roll_dice()

    print(f"die1 in main() is still: {die1}")


if __name__ == '__main__':
    main()
