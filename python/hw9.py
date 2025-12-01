# Dice Rolling Simulator. Use the random module to create a function that simulates rolling two six-sided dice and returns their sum.
# Then, create a program that asks the user how many times to roll the dice and uses a dictionary to track and display the frequency of each sum
import random


def roll_dice() -> int:
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    print(f"Rolled: {die1} + {die2} = {die1 + die2}")
    return die1 + die2


def simulate_rolls(num_rolls: int) -> dict[int, int]:
    frequency: dict[int, int] = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        result: int = roll_dice()
        frequency[result] += 1

    return frequency


def main() -> None:
    num_rolls: int = int(input("Enter the number of times to roll the dice: "))
    if num_rolls <= 0:
        print("Please enter a positive integer.")
        return

    frequency: dict[int, int] = simulate_rolls(num_rolls)

    print("\nSum\tFrequency")
    for sum_value, freq in frequency.items():
        print(f"{sum_value}\t{freq}")


main()
