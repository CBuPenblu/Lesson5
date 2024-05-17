class Warrior():
    def __init__(self, name, power, health, endurance, skin_color):
        self.name = name
        self.power = power
        self.health = health
        self.endurance = endurance
        self.skin_color = skin_color

    def sleep(self):
        print(f"{self.name} went to sleep")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} eating")
        self.health += 1

    def hit(self):
        print(f"{self.name} hitting someone")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} walking")

    def info(self):
        print(f" warrior name is - {self.name}")
        print(f" warrior skin color is - {self.skin_color}")
        print(f" warrior power is - {self.power}")
        print(f" warrior endurance is - {self.endurance}")
        print(f" warrior health is - {self.health}")