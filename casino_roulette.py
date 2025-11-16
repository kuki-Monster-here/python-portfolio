import random

number = random.randint(1, 10)
guess = int(input("Угадай число от 1 до 10: "))

if guess == number:
    print("Ты выиграл! 🎉")
else:
    print(f"Не угадал! Загаданное число: {number}")
