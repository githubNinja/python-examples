print("Let's start rock , paper and scissors")
player1 = input("Player1 enter your choice::")
player2 = input("Player2 enter your choice::\n")
if player1 == "rock" and player2 == "scissors":
    print("Player1 wins !!")
if player1 == "scissors" and player2 == "paper":
    print("Player1 wins !!")
elif player1 == "rock" and player2 == "paper":
    print("\n Player2 wins !!")
if player1 == player2:
    print("\n It's a tie")