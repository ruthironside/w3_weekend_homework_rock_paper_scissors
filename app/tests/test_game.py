import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        # self.game.move_choice1 [0] = rock
        # self.game.move_choice2 [1] = paper
        # self.game.move_choice3 [2] = scissors

        self.game.moves = ["rock", "paper", "scissors"]

    def test_game_has_player(self):
        self.assertEqual()

    # def test_play_game(self):
    #     player1 = Player("Betty", self.paper)
    #     player2 = Player("Bunty", self.rock)
    #     self.game.play_game(player1, player2)

