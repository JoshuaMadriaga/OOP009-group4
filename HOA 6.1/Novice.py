from Character import Character

class Novice(Character):
    def __init__(self, username):
        super().__init__(username)
        self.__mana = 0

    def getMana(self):
        return self.__mana

    def setMana(self, mana):
        self.__mana = mana

    def basicAttack(self, character):
        character.reduceHp(self.getBasic())
        print(f"{self.getUsername()} performs Basic Attack! - {self.getDamage()}")
        self.regenerate_mana()

    def choose_attack(self, character):
        print("Available Attacks:")
        print("1. Basic Attack")
        print("2. Special Attack (requires 30 mana)")
        print("3. Ultimate Attack (requires 50 mana)")
        choice = input("Choose your attack (1, 2, or 3): ")
        if choice == "1":
            self.basicAttack(character)
        elif choice == "2":
            self.specialAttack(character)
        elif choice == "3":
            self.ultimateAttack(character)
        else:
            print("Invalid choice! Using Basic Attack.")
            self.basicAttack(character)

    def specialAttack(self, character):
        print("Special Attack not implemented for this character.")

    def regenerate_mana(self):
        self.setMana(min(100, self.getMana() + 10))  # Regenerate 10 mana, capped at 100