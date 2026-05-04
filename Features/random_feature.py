import random

def roll_dice():
    result = random.randint(1, 6)
    print(f"Du hast eine {result} gewürfelt!")

if __name__ == "__main__":
    roll_dice()
