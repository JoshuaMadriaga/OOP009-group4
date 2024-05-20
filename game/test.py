from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

Character1=Swordsman("royce")
Character2=Magician("archie")
Character3=Archer("sev")
Character4=Boss("Final Boss")
print(f"{Character1.getUsername()} HP: {Character1.getHp()}")
print(f"{Character2.getUsername()} HP: {Character2.getHp()}")
print(f"{Character3.getUsername()} HP: {Character3.getHp()}")
Character1.slashAttack(Character4)
Character3.rangedAttack(Character4)
Character4.basicAttack(Character1)
Character4.basicAttack(Character2)
Character4.basicAttack(Character3)
print(f"{Character1.getUsername()} HP: {Character1.getHp()}")
print(f"{Character2.getUsername()} HP: {Character2.getHp()}")
print(f"{Character3.getUsername()} HP: {Character3.getHp()}")
Character2.heal()
Character2.magicAttack(Character4)
print(f"{Character1.getUsername()} HP: {Character1.getHp()}")
print(f"{Character2.getUsername()} HP: {Character2.getHp()}")
print(f"{Character3.getUsername()} HP: {Character3.getHp()}")