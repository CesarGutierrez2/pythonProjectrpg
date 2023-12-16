import random


# i create a class called humanoids with the given attributes
class Humanoids:
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom,
                 charisma):
        # the __init__ method initializes the attributes and sets some attributes randomly and others for user input
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = random.randint(1, 18)
        self.dexterity = random.randint(1, 18)
        self.constitution = random.randint(1, 18)
        self.intelligence = random.randint(1, 18)
        self.wisdom = random.randint(1, 18)
        self.charisma = random.randint(1, 18)


# this defines a class called humans that inherits from humanoids, representing
# a specific race of humanoids
class Humans(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color):
        # calls the parent class humanoids to initialize the common attributes
        super().__init__(height, weight, hair_color, eye_color, 0, 0, 0, 0, 0, 0)
        # this is specific to humans which allows the +2 to one of the attributes
        self.choose_attribute_bonus()

    # this method presents the user with attribute choices and their corresponding numbers
    def choose_attribute_bonus(self):
        attribute_choices = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        print("You chose to be a Human! You can add +2 to one of the following attributes: ")
        for i, attribute in enumerate(attribute_choices, 1):
            print(f"{i}. {attribute}")

        choice = int(input("Enter the number corresponding to your choice: "))
        chosen_attribute = attribute_choices[choice - 1]
        setattr(self, chosen_attribute, getattr(self, chosen_attribute) + 2)


# creating another class called elves that inherit from the humanoids class
class Elves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color):
        super().__init__(height, weight, hair_color, eye_color, 0, 0, 0, 0, 0, 0)
        # the specific attribute points for this class
        self.resistance_to_sleep = 100
        self.dexterity += 2
        self.charisma += 2


# another class that inherits from the parent class humanoids
class Dwarves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color):
        super().__init__(height, weight, hair_color, eye_color, 0, 0, 0, 0, 0, 0)
        # their special attributes
        self.resistance_to_magic = 20
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2


# this function prompts the user to choose a race and enter values for height,
# weight, hair color and eye color
def characterCreation():
    race = input("Choose your race (Humans/Elf/Dwarf): ").capitalize()
    height = int(input("Enter the height (from 4ft-7ft):"))
    weight = int(input("Enter the weight (from 60 - 300lbs): "))
    hair_color = input("Enter hair color: ")
    eye_color = input("Enter eye color: ")

    # based on the users choice, an instance of the corresponding class is created
    # with the previously generated values

    if race == 'Human':
        character = Humans(height, weight, hair_color, eye_color)
    elif race == 'Elf':
        character = Elves(height, weight, hair_color, eye_color)
    elif race == 'Dwarf':
        character = Dwarves(height, weight, hair_color, eye_color)
    else:
        print("Unknown race. Please choose Human, Elf, or Dwarf.")
        return

# finally this function prints the details of the generated character

    print(f"\nYour character stats:\n"
          f"Race: {race}\n"
          f"Height: {character.height}ft\n"
          f"Weight: {character.weight}lbs\n"
          f"Hair Color: {character.hair_color}\n"
          f"Eye Color: {character.eye_color}\n"
          f"Strength: {character.strength}\n"
          f"Dexterity: {character.dexterity}\n"
          f"Constitution: {character.constitution}\n"
          f"Intelligence: {character.intelligence}\n"
          f"Wisdom: {character.wisdom}\n"
          f"Charisma: {character.charisma}\n")


if __name__ == "__main__":
    def main():
        characterCreation()


    main()
