import unittest
# from unittest.mock import Mock, MagicMock, call
from NumberBaseball import Game

class NumberBaseballTest(unittest.TestCase):

    def test_guess_correct_answer_then_3S(self):
        game = Game("369")
        result = game.guess_checker("369")
        self.assertEqual("3S", result)

        game1 = Game("106")
        result1 = game1.guess_checker("106")
        self.assertEqual("3S", result1)