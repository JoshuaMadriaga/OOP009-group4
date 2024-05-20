from Novice import Novice

class Swordsman(Novice):
    def __init(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp()+self.getVit())
    
    def slashAttack(self, character):
        self.new_damage = self.getDamage()+self.getStr()
        character.reduceHp(self.new_damage)
        print(f"[self.getUsername()] performed slash Attack! - {self.new_damage}")
        