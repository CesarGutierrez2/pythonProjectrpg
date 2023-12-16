#i create a class called player character
class PlayerCharacter:
    def __init__(self, health, armor_rating, attack_power): #the attributes of the class
        self.set_health(health)
        self.set_armor_rating(armor_rating)
        self.set_attack_power(attack_power)

    def set_health(self, health): # setting the health attribute and making sure it is a number between 1-100
        if 1 <= health <= 100:
            self.health = health
        else:
            print("Health value must be between 1 and 100. Try again!")#else value if health is not between 1 and 100
            self.health = None

    def set_armor_rating(self, armor_rating):#setting up the armor rating attribute and making sure it is a number between 1-20
        if 1 <= armor_rating <= 20:
            self.armor_rating = armor_rating
        else:
            print("No! Armor rating must be between 1 and 20.")
            self.armor_rating = None

    def set_attack_power(self, attack_power):#setting up the attack rating attribute and making sure it is a number between 1-20
        if 1 <= attack_power <= 20:
            self.attack_power = attack_power
        else:
            print("Invalid! Attack power must be between 1 and 20.")
            self.attack_power = None

    def get_health(self):#this method returns the health attribute whenever it is called
        return self.health

    def get_armor_rating(self):#this method is the same as get_health() but it returns the armor rating
        return self.armor_rating

    def get_attack_power(self):
        return self.attack_power


def main(): #this is the main function which is the entry point of the program
    health = int(input("Enter the health rating (1-100): "))#asking for the users input
    armor_rating = int(input("Enter the armor rating (1-20): "))
    attack_power = int(input("Enter the attack rating (1-20): "))

    wizard = PlayerCharacter(health, armor_rating, attack_power)#this creates a wizard object with the health, armor rating, and attack rating attributes

    # printing the wizards attributes depending on the user input
    print("\nHere are your characters attributes: ")
    print("Wizards health", wizard.get_health())
    print("Armor rating:", wizard.get_armor_rating())
    print("Attack power:", wizard.get_attack_power())


if __name__ == "__main__":
    main()
