products = [
    {"название": "Телефон", "цена": 20000, "в_наличии": True},
    {"название": "Ноутбук", "цена": 50000, "в_наличии": False}
]

for product in products:
    if product["в_наличии"]:
        print(f"{product['название']} - {product['цена']} руб.")
