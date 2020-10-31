import unittest
from app.models.game import *
from app.models.player import *

class TestGame(unittest.TestCase):
    def setUp(self):

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

    def test_game_player1_wins_with_scissors(self):
        result = self.game1.play_game(self.player_scissors.choice, self.player_paper.choice)
        self.assertEqual("Player 1 wins!", result)

    def test_game_player1_wins_with_paper(self):
        result = self.game1.play_game(self.player_paper.choice, self.player_rock.choice)
        self.assertEqual("Player 1 wins!", result)

    def test_game_player2_wins_with_paper(self):
        result = self.game1.play_game(self.player_rock.choice, self.player_paper.choice)
        self.assertEqual("Player 2 wins!", result)

    def test_game_player2_wins_with_rock(self):
        result = self.game1.play_game(self.player_scissors.choice, self.player_rock.choice)
        self.assertEqual("Player 2 wins!", result)

    def test_game_player2_wins_with_scissors(self):
        result = self.game1.play_game(self.player_paper.choice, self.player_scissors.choice)
        self.assertEqual("Player 2 wins!", result)

    def test_game_draw_with_rock(self):
        result = self.game1.play_game(self.player_rock.choice, self.player_rock.choice)
        self.assertEqual("Draw!", result)

    def test_game_draw_with_scissors(self):
        result = self.game1.play_game(self.player_scissors.choice, self.player_scissors.choice)
        self.assertEqual("Draw!", result)

    def test_game_draw_with_paper(self):
        result = self.game1.play_game(self.player_paper.choice, self.player_paper.choice)
        self.assertEqual("Draw!", result)

