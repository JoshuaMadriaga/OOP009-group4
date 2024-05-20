from Novice import Novice
import random

class Magician(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setInt(15)

    def heal(self):
        heal_amount = self.getInt() * 2
        self.addHp(heal_amount)
        print(f"{self.getUsername()} performed Heal! + {heal_amount}")
        self.regenerate_mana()

    def specialAttack(self, character):
        if self.getMana() >= 40:
            self.setMana(self.getMana() - 40)
            self.heal()
        else:
            print("Not enough mana to perform Special Attack!")

    def ultimateAttack(self, character):
        if self.getMana() >= 50:
            self.setMana(self.getMana() - 50)
            damage = random.randint(70, 120)
            character.reduceHp(damage)
            print(f"{self.getUsername()} performs Ultimate Attack! - {damage}")
            self.regenerate_mana()
        else:
            print("Not enough mana to perform Ultimate Attack!")