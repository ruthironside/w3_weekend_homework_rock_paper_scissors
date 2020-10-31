import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        # self.game.move_choice1 [0] = rock
        # self.game.move_choice2 [1] = paper
        # self.game.move_choice3 [2] = scissors

        self.player_rock = Player("Bill", "rock")
        self.player_paper = Player("Ben", "paper")
        self.player_scissors = Player("Betty", "scissors")

        self.game1 = Game(self.player_rock, self.player_scissors)

    def test_game_has_players(self):
        self.assertEqual(self.player_rock, self.game1.player1)
        self.assertEqual(self.player_scissors, self.game1.player2)

    def test_game_player1_wins_with_rock(self):
        result = self.game1.play_game(self.player_rock.choice, self.player_scissors.choice)
        self.assertEqual("Player 1 wins!", result)

    # def test_play_game(self):
    #     player1 = Player("Betty", self.paper)
    #     player2 = Player("Bunty", self.rock)
    #     self.game.play_game(player1, player2)

