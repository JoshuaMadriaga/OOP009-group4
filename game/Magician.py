from Novice import Novice


class Magician(Novice):
    def __init(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp()+self.getVit())
        
    def heal(self):
        self.addHp(self.getInt())
        print(f"{self.getUsername()} performed Heal! + {self.getInt()}")
    
    def magicAttack(self, character):
        self.new_damage = self.getDamage()+self.getInt()
        character.reduceHp(self.new_damage)
        print(f"[self.getUsername()] performed slash Attack! - {self.new_damage}")
        