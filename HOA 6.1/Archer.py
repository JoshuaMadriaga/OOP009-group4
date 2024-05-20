from Novice import Novice
import random

class Archer(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setAgi(20)

    def rainingArrow(self, character):
        damage = random.randint(20, 40)
        character.reduceHp(damage)
        print(f"{self.getUsername()} performs Raining Arrow! - {damage}")
        self.regenerate_mana()

    def specialAttack(self, character):
        if self.getMana() >= 20:
            self.setMana(self.getMana() - 20)
            self.rainingArrow(character)
        else:
            print("Not enough mana to perform Special Attack!")

    def ultimateAttack(self, character):
        if self.getMana() >= 50:
            self.setMana(self.getMana() - 50)
            damage = random.randint(60, 100)
            character.reduceHp(damage)
            print(f"{self.getUsername()} performs Ultimate Attack! - {damage}")
            self.regenerate_mana()
        else:
            print("Not enough mana to perform Ultimate Attack!")
