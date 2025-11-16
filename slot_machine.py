import random

symbols = ["🍒", "🍋", "⭐", "💎", "7️⃣"]

def spin():
    return [random.choice(symbols) for _ in range(3)]

result = spin()
print("Результат:", " ".join(result))

if result[0] == result[1] == result[2]:
    print("ДЖЕКПОТ! 🎰")
