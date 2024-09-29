#Python Slot Machine with difficulty
import random

class SlotMachine:
    def __init__(self,start_money):
        self.money = start_money
        self.symbols = ['🍒','🍊','🍋','🔔','🍫']

    def spin_row(self):
        return [random.choice(self.symbols) for _ in range(3)]

    def play(self,bet,difficulty):
        if bet > self.money:
            print("You don't have enough money to place the bet :(")
            return
        self.money -= bet
        result = self.spin_row()
        print(f"Spinning....")
        print("**************")
        print(" | ".join(result))
        print("**************")

        if difficulty == "easy":
            if result[0] == result[1] == result[2]:
                money_won = bet * 5
                self.money += money_won
                print(f"Congrats! You won {money_won} Rs")
            else:
                print("Sorry :( , You lost")
        elif difficulty == "hard":
            if result[0] == result[1] == result[2]:
                money_won = bet * 20
                self.money += money_won
                print(f"Congrats! You won {money_won} Rs")
            else:
                print("Sorry :( , You lost")
        print(f"Current Balance : {self.money}Rs")

#main
def main():
    while True:
        start_money = int(input("Enter the money u have to gamble (in Rs) : "))
        if start_money <= 0:
            print("Money must be greater than 0")
            continue
        player1 = SlotMachine(start_money)

        print("***************************")
        print("Welcome to the Slot Machine")
        print("***************************")
        print(f"You start with {start_money} Rs")

        while player1.money > 0:
            bet = int(input("Place ur bet (in Rs): "))
            if bet <= 0:
                print("Bet must be greater than 0")
                continue
            difficulty = input("Enter the difficulty (easy/hard) : ")
            if difficulty not in ["easy", "hard"]:
                print("Invalid choice !")
                continue
            player1.play(bet,difficulty)

        print("Game Over ! You ran out of money :-(")

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

if __name__ == "__main__":
    main()