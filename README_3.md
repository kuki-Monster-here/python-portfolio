### 🔰 **Уровень 1: Основы Python**

#### 1. **`hello_world.py`** - "Привет, мир!"

```python
print("Привет, мир!")

```
#### 2. **`calculator.py`** - Калькулятор

```python
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
```
#### 3. **`weather_advisor.py`** - Погодный советчик

```python
weather = "солнечно"

if weather == "солнечно":
    print("Идём гулять!")
else:
    print("Сидим дома.")

```
#### 4. **`counter.py`** - Счётчик

```python
for i in range(1, 6):
    print(i)

```
#### 5. **`infinite_loops.py`** - Бесконечные циклы

```python
# Бесконечный дождь из смайлов
while True:
    print("☔", end=" ")
   
```
#### 🛠️  **Уровень 2: Функции и логика**

#### 6. **`functions.py`** - Функции с параметрами

```python
def launch_fireworks(count):
    print(f"🎆 Запускаем {count} фейерверков...")
    print("Ура! " + "✨" * count)

launch_fireworks(3)

```
#### 7. **`password_generator.py`** - Генератор паролей
```python
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

print("Новый пароль:", generate_password())

```
#### 8. **`temperature_converter.py`** - Конвертер температур

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print("20°C =", celsius_to_fahrenheit(20), "°F")

```
#### 9. **`min_max_finder.py`** - Поиск min/max в списках

```python
def find_min(numbers):
    return min(numbers)

def find_max(numbers):
    return max(numbers)

numbers = [5, 2, 8, 1, 9]
print("Минимальное:", find_min(numbers))
print("Максимальное:", find_max(numbers))

```
#### 10. **`even_checker.py`** - Проверка чётности

```python
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False

```
####🗃️ **Уровень 3: Структуры данных**

#### 11. **`task_manager.py`** - Менеджер задач

```python
tasks = ["купить хлеб", "позвонить маме"]
task_status = {
    "купить хлеб": "не сделано",
    "позвонить маме": "в процессе"
}

# Добавление задачи
def add_task(task, status="не сделано"):
    tasks.append(task)
    task_status[task] = status

add_task("сделать ДЗ")
print("Задачи:", tasks)
print("Статусы:", task_status)

```
#### 12. **`library_system.py`** - Библиотека книг

```python
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

```
#### 13. **`tic_tac_toe.py`** - Игровое поле (крестики-нолики)

```python
board = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", "X"]
]

for row in board:
    print("|" + "|".join(row) + "|")

```
#### 14. **`product_catalog.py`** - Каталог товаров

```python
products = [
    {"название": "Телефон", "цена": 20000, "в_наличии": True},
    {"название": "Ноутбук", "цена": 50000, "в_наличии": False}
]

for product in products:
    if product["в_наличии"]:
        print(f"{product['название']} - {product['цена']} руб.")

```
#### 🎮 **`Уровень 4: Игры и развлечения`**

#### 15. **`casino_roulette.py`** - Казино-рулетка

```python
import random

number = random.randint(1, 10)
guess = int(input("Угадай число от 1 до 10: "))

if guess == number:
    print("Ты выиграл! 🎉")
else:
    print(f"Не угадал! Загаданное число: {number}")

```
#### 16. **`guess_number.py`** - Угадай число

```python
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

```
#### 17. **`blackjack.py`** - Блэкджек (21)

```python
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(cards)

player_hand = [cards.pop(), cards.pop()]
dealer_hand = [cards.pop(), cards.pop()]

print(f"Твои карты: {player_hand}, сумма: {sum(player_hand)}")
print(f"Карты дилера: [{dealer_hand[0]}, ?]")

```
#### 18. **`slot_machine.py`** - Игровой автомат

```python
import random

symbols = ["🍒", "🍋", "⭐", "💎", "7️⃣"]

def spin():
    return [random.choice(symbols) for _ in range(3)]

result = spin()
print("Результат:", " ".join(result))

if result[0] == result[1] == result[2]:
    print("ДЖЕКПОТ! 🎰")

```
#### 🧠 **Уровень 5: Продвинутые темы**

#### 19. **`recursive_lists.py`** - Рекурсивные списки

```python
weird_list = [1, 2, 3]
weird_list.append(weird_list)
print(weird_list)  # [1, 2, 3, [...]]

```
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
