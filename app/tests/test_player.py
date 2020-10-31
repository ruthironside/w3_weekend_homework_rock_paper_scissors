import unittest

from app.models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Bill", "rock")
        self.player2 = Player("Ben", "scissors")

    def test_player_has_name(self):
        self.assertEqual("Bill", self.player1.name)

    def test_plauyer_has_choice(self):
        self.assertEqual("scissors", self.player2.choice)