class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

def play_game(self, player1, player2):

    if player1 == player2:
        result = 'Draw!'
    elif player1 == 'rock' and player2 == 'paper':
        result = 'player2 wins!'
    elif player1 == 'rock' and player2 == 'scissors':
        result = 'player1 wins!'
    elif player1 == 'paper' and player2 == 'rock':
        result = 'player1 wins!'
    elif player == 'paper' and computer == 'scissors':
        result = 'player2 wins!'
    elif player == 'scissors' and computer == 'rock':
        result = 'player2 wins!'
    elif player == 'scissors' and computer == 'paper':
        result = 'player1 wins!'

    return result