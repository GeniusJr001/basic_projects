import random
#computer function
def play():
    user = input("(R) for rock,(P) for Paper, (S) for Scissors").lower
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "tie"
    elif is_win(user, computer):
        return "You won"
    else:
            return "you lost"
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player =="s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    
print(play())
