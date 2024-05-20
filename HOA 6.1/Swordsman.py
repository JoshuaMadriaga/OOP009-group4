from Novice import Novice
import random

class Swordsman(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp() + self.getVit())

    def daggerStrike(self, character):
        damage = self.getStr() * 2
        character.reduceHp(damage)
        print(f"{self.getUsername()} performs Dagger Strike! - {damage}")
        self.regenerate_mana()

    def specialAttack(self, character):
        if self.getMana() >= 30:
            self.setMana(self.getMana() - 30)
            damage = random.randint(30, 50)
            self.daggerStrike(character)
            character.reduceHp(damage)
            print(f"{self.getUsername()} performs Ultimate Attack! - {damage}")
            self.regenerate_mana()
        else:
            print("Not enough mana to perform Special Attack!")

    def ultimateAttack(self, character):
        if self.getMana() >= 50:
            self.setMana(self.getMana() - 50)
            damage = random.randint(50, 100)
            character.reduceHp(damage)
            print(f"{self.getUsername()} performs Ultimate Attack! - {damage}")
            self.regenerate_mana()
        else:
            print("Not enough mana to perform Ultimate Attack!")