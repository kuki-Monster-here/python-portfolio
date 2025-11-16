🔰 Уровень 1: Основы Python


1. "Привет, мир!"

print("Привет, мир!")

hello_world.py


2.  Калькулятор

a = 5

b = 3

print(f"{a} + {b} = {a + b}")

calculator.py


3. Погодный советчик
   
weather = "солнечно"

if weather == "солнечно":
    
 print("Идём гулять!")

else:
    
   print("Сидим дома.")

weather_advisor.py 


4. Счётчик
   
for i in range(1, 6):
   
   print(i)

counter.py


5. Бесконечные циклы

Бесконечный дождь из смайлов

while True:

   print("☔", end=" ")
   

🛠️ Уровень 2: Функции и логика

6. Функции с параметрами
   
def launch_fireworks(count):

   print(f"🎆 Запускаем {count} фейерверков...")
  
   print("Ура! " + "✨" * count)

launch_fireworks(3)

functions.py


7. Генератор паролей
   
import random

import string

def generate_password(length=8):

   characters = string.ascii_letters + string.digits
   
   return ''.join(random.choice(characters) for _ in range(length))

print("Новый пароль:", generate_password())

password_generator.py


8. Конвертер температур
   
def celsius_to_fahrenheit(celsius):
   
   return celsius * 9/5 + 32

print("20°C =", celsius_to_fahrenheit(20), "°F")

temperature_converter.py


9. Поиск min/max в списках
    
def find_min(numbers):

   return min(numbers)

def find_max(numbers):

   return max(numbers)

numbers = [5, 2, 8, 1, 9]

print("Минимальное:", find_min(numbers))

print("Максимальное:", find_max(numbers))

min_max_finder.py


10. Проверка чётности

def is_even(number):
    
   return number % 2 == 0

print(is_even(4))  # True

print(is_even(5))  # False

even_checker.py


🗃️ Уровень 3: Структуры данных

11. Менеджер задач
    
tasks = ["купить хлеб", "позвонить маме"]

task_status = {
    
   "купить хлеб": "не сделано",
   
   "позвонить маме": "в процессе"

}

Добавление задачи

def add_task(task, status="не сделано"):
    
   tasks.append(task)
    
   task_status[task] = status

add_task("сделать ДЗ")

print("Задачи:", tasks)

print("Статусы:", task_status)


12. Библиотека книг
    
library = {
    
   "1984": {
        
   "автор": "Джордж Оруэлл",
   
   "жанр": "антиутопия", 
   
   "год": 1949
   
   },
    
   "Гарри Поттер": {
   
   "автор": "Дж.К. Роулинг",
        
   "жанр": "фэнтези",
        
   "год": 1997
    
   }

}

print(library["1984"]["автор"])  # Джордж Оруэлл

library_system.py


13. Игровое поле (крестики-нолики)

board = [
    
   ["X", "O", " "],
    
   [" ", "X", " "], 
    
   ["O", " ", "X"]

]

for row in board:
    
   print("|" + "|".join(row) + "|")

tic_tac_toe.py


14. Каталог товаров
    
products = [
    
   {"название": "Телефон", "цена": 20000, "в_наличии": True},
    
   {"название": "Ноутбук", "цена": 50000, "в_наличии": False}

]

for product in products:
    
   if product["в_наличии"]:
        
   print(f"{product['название']} - {product['цена']} руб.")

product_catalog.py


 🎮 Уровень 4: Игры и развлечения

15. Казино-рулетка
 
import random

number = random.randint(1, 10)

guess = int(input("Угадай число от 1 до 10: "))

if guess == number:
    print("Ты выиграл! 🎉")

else:
    
   print(f"Не угадал! Загаданное число: {number}")

casino_roulette.py


16. Угадай число
    
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

guess_number.py 


17. blackjack.py - Блэкджек (21)

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(cards)

player_hand = [cards.pop(), cards.pop()]

dealer_hand = [cards.pop(), cards.pop()]

print(f"Твои карты: {player_hand}, сумма: {sum(player_hand)}")

print(f"Карты дилера: [{dealer_hand[0]}, ?]")

blackjack.py 


18. Игровой автомат

import random

symbols = ["🍒", "🍋", "⭐", "💎", "7️⃣"]

def spin():
    
   return [random.choice(symbols) for _ in range(3)]

result = spin()

print("Результат:", " ".join(result))

if result[0] == result[1] == result[2]:
    
   print("ДЖЕКПОТ! 🎰")

slot_machine.py


🧠 Уровень 5: Продвинутые темы

19. Рекурсивные списки

weird_list = [1, 2, 3]

weird_list.append(weird_list)

print(weird_list)  # [1, 2, 3, [...]]

recursive_lists.py


#### 20. **`closures.py`** - Замыкания

```python
def multiplier(factor):
    def inner(number):
        return number * factor
    return inner

double = multiplier(2)
print(double(5))  # 10

```
#### 21. **`decorators.py`** - Декораторы
```python
def log_time(func):
    def wrapper(*args):
        print(f"Запуск {func.__name__}...")
        result = func(*args)
        print("Готово!")
        return result
    return wrapper

@log_time
def calculate(a, b):
    return a + b

print(calculate(2, 3))








