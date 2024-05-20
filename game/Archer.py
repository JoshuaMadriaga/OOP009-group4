from Novice import Novice
import random

class Archer(Novice):
    def __init(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp()+self.getVit())
    
    def rangedAttack(self, character):
        self.new_damage = self.getDamage()+random.randint(0,self.getInt())
        character.reduceHp(self.new_damage)
        print(f"[self.getUsername()] performed slash Attack! - {self.new_damage}")
        