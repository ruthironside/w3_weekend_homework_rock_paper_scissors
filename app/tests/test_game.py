import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        # self.game.move [0] = rock
        # self.game.move [1] = paper
        # self.game.move [2] = scissors

        choices = ["rock", "paper", "scissors"]

    def test_play_game(self):
        player1 = Player("Betty", self.paper)
        player2 = Player("Bunty", self.rock)
        self.game.play_game(player1, player2)

