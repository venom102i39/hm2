class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print(f"Назва товару: {self.name}")
        print(f"Ціна за одиницю: {self.price} грн")
        print(f"Кількість: {self.quantity} шт")
        print(f"Загальна вартість: {self.calculate_total_price()} грн")
apple = Product("Яблуко", 15, 10)
apple.display_info()
