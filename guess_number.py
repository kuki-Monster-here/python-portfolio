import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    attempts += 1
    
    if guess < secret_number:
        print("Больше!")
    elif guess > secret_number:
        print("Меньше!")
    else:
        print(f"Поздравляю! Угадал за {attempts} попыток!")
        break
