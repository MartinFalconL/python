# Aprendiendo logica booleana
play1 = str(input ("enter player 1 choice:"))
play2 = str(input ("enter player 2 choice:"))

if play1 != ("rock" or "paper" or "scissors") and play2 != ("rock" or "paper" or "scissors"):
    print ("invalid options")
else:
    if play1 == "rock" and play2 == "rock":
        print ("TIE!!")
    elif play1 == "paper" and play2 == "rock":
        print ("player1 wins!!")
    elif play1 == "scissors" and play2 == "rock":
        print ("player2 wins!!")
    elif play1 == "rock" and play2 == "paper":
        print ("player2 wins!!")
    elif play1 == "paper" and play2 == "paper":
        print ("TIE!!")
    elif play1 == "scissors" and play2 == "paper":
        print("player1 wins!!")
    elif play1 == "rock" and play2 == "scissors":
        print ("player1 wins!!")
    elif play1 == "paper" and play2 == "scissors":
        print ("player2 wins!!")
    else: print ("TIE")