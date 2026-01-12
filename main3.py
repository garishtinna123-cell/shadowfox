class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)
        print()

    def is_leader(self):
        if self.name == "Captain America":
            print(self.name, "is the Leader of Avengers\n")
        else:
            print(self.name, "is not the Leader\n")


# Creating Avengers objects
avenger1 = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
avenger2 = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
avenger3 = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
avenger4 = Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon")
avenger5 = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir")
avenger6 = Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows")

# Display information
avengers = [avenger1, avenger2, avenger3, avenger4, avenger5, avenger6]

for hero in avengers:
    hero.get_info()
    hero.is_leader()