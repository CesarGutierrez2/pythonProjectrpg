class PlayerCharacter:
    def __init__(self, health, armor_rating, attack_power):
        self.set_health(health)
        self.set_armor_rating(armor_rating)
        self.set_attack_power(attack_power)

    def set_health(self, health):
        if 1 <= health <= 100:
            self.health = health
        else:
            print("Health value must be between 1 and 100. Try again!")

    def set_armor_ranking(self, armor_rating):
        if 1 <= armor_rating <= 20:
            self.armor_rating = armor_rating
        else:
            print("No! Armor rating must be between 1 and 20.")

    def attack_power(self, attack_power):
        if 1 <= attack_power <= 20:
            self.attack_power = attack_power
        else:
            print("Invalid! Attack power must be between 1 and 20.")

    def get_health(self):
        return self.health

    def get_armor_rating(self):
        return self.armor_rating

    def get_attack_power(self):
        return self.attack_power


def main():
    health = int(input("Enter the health rating (1-100): "))
    armor_rating = int(input("Enter the armor rating (1-20): "))
    attack_power = int(input("Enter the attack rating (1-20): "))

    Wizard = PlayerCharacter(health, armor_rating, attack_power)

    # printing the wizards attributes
    print("Here are your characters attributes: ")
    print("Wizards health", Wizard.get_health())
    print("Armor rating:", Wizard.get_armor_rating())
    print("Attack power:", Wizard.get_attack_power())


if __name__ == "__main__":
    main()
