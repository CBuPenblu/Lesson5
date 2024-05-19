class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        items_list = ', '.join([f"{item}: ${price:.2f}" for item, price in self.items.items()])
        return f"Store: {self.name}\nAddress: {self.address}\nItems: {items_list}"

store1 = Store("Fresh BaBanana", "123 Grocery St")
store2 = Store("Tech Haven", "456 Tech Blvd")
store3 = Store("Book Nuken", "769 Book Ln")

store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("oranges", 0.65)

store2.add_item("laptop", 999.99)
store2.add_item("smartphone", 699.99)
store2.add_item("headphones", 199.99)

store3.add_item("fiction book", 15.99)
store3.add_item("non-fiction book", 12.99)
store3.add_item("magazine", 5.99)

print(store1)
print()
print(store2)
print()
print(store3)

# Пример удаления товара
store1.remove_item("bananas")
print("\nAfter removing bananas from Fresh BaBanana:")
print(store1)

# Пример получения цены товара
print("\nPrice of laptop in Tech Haven:", store2.get_price("laptop"))

# Пример обновления цены товара
store3.update_price("fiction book", 13.99)
print("\nAfter updating the price of fiction book in Book Nuken:")
print(store3)
