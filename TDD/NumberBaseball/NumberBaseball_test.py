import unittest
from NumberBaseball import Game

class NumberBaseballTest(unittest.TestCase):
    game = Game()

    def test_guess_correct_answer_then_3S(self):
        guess = "369"
        result = self.game.guess_checker(guess)
        self.assertEqual("3S", result)