from Swordsman import Swordsman
from Magician import Magician
from Archer import Archer
import random

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.bot_characters = [Swordsman("Bot"), Archer("Bot"), Magician("Bot")]

    def start_game(self):
        print("Welcome to the Game!")
        mode = input("Choose the game mode:\n1. Player vs Player\n2. Player vs Computer\nEnter your choice (1 or 2): ")
        
        if mode == "1":
            print("Player 1, choose your character:")
            self.player1 = self.choose_character()
            print("Player 2, choose your character:")
            self.player2 = self.choose_character()
        elif mode == "2":
            print("Player 1, choose your character:")
            self.player1 = self.choose_character()
            print("Computer is choosing its character...")
            self.player2 = self.choose_bot_character()
        else:
            print("Invalid choice! Please try again.")
            self.start_game()

        while self.player1.getHp() > 0 and self.player2.getHp() > 0:
            print("\n" + "=" * 30)
            print(f"{self.player1.getUsername()} ({self.player1.__class__.__name__}) HP: {self.player1.getHp()} | Mana: {self.player1.getMana()}")
            print(f"{self.player2.getUsername()} ({self.player2.__class__.__name__}) HP: {self.player2.getHp()} | Mana: {self.player2.getMana()}")
            print("=" * 30)
            print(f"{self.player1.getUsername()}'s Turn:")
            self.player1.choose_attack(self.player2)
            if self.player2.getHp() <= 0:
                break
            print(f"{self.player2.getUsername()}'s Turn:")
            self.player2.choose_attack(self.player1)

        print("\n" + "=" * 30)
        if self.player1.getHp() <= 0:
            print(f"{self.player2.getUsername()} wins!")
        else:
            print(f"{self.player1.getUsername()} wins!")
        print("=" * 30)

    def choose_character(self):
        print("\nAvailable Characters:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Magician")
        choice = input("Choose your character (1, 2, or 3): ")
        username = input("Enter your username: ")
        if choice == "1":
            return Swordsman(username)
        elif choice == "2":
            return Archer(username)
        elif choice == "3":
            return Magician(username)
        else:
            print("Invalid choice! Please try again.")
            return self.choose_character()

    def choose_bot_character(self):
        bot_character = random.choice(self.bot_characters)
        print(f"Computer has chosen {bot_character.__class__.__name__} as its character.")
        return bot_character

if __name__ == "__main__":
    game = Game()
    game.start_game()