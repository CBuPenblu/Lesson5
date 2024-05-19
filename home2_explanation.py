class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Item {item_name} has been added in {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Item {item_name} was added in {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Item price {item_name} updated in {self.name}")
        else:
            print(f"Item {item_name} is not found")

store1 = Store("Crazy banana", "Banana street 40")
store2 = Store("Fruity noob", "Noob street 69")
store3 = Store("Spinner", "Wheel avenue 101")

store1.add_item("bread", 2)
store1.add_item("tomatoes", 3.5)
store1.add_item("chicken breasts", 4.40)

store1.remove_item("bread")

print(store1.get_price("tomatoes"))

store1.update_price("chicken breasts", 4.20)