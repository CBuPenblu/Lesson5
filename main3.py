class Warrior():
    def __init__(self, name, power, health, endurance, skin_color):
        self.name = name
        self.power = power
        self.health = health
        self.endurance = endurance
        self.skin_color = skin_color

    def sleep(self):
        print(f"{self.name} went to sleep")
        self.power += 2

    def eat(self):
        print(f"{self.name} eating")
        self.health += 2
        self.endurance += 3

    def hit(self):
        print(f"{self.name} hitting someone")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} walking")
        self.power -= 1

    def info(self):
        print(f" warrior name is - {self.name}")
        print(f" warrior skin color is - {self.skin_color}")
        print(f" warrior power is - {self.power}")
        print(f" warrior endurance is - {self.endurance}")
        print(f" warrior health is - {self.health}")

war1 = Warrior("CBuPenbIu", 50, 100, 300, "white")
war2 = Warrior("MAKAPOHbI", 75, 150, 450, "brown")

war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()

war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()

