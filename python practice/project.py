import random

def play():
    user = input("Pick 'r' for rock, 'p' for paper, 's' for scissors\n")
    com = random.choice(['r', 'p', 's'])

    if user == com:
        return 'tie'

 
    if is_win(user, com):
        return 'You win'

    return 'You lose'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())