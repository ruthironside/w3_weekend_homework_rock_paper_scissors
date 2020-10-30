from app.models.player import *



player1 = Player("Bill", "rock")
player2 = Player("Ben", "scissors")

players = [player1, player2]


def add_new_player(player):
    players.append(player)