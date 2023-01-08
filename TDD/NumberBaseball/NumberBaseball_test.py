import unittest
# from unittest.mock import Mock, MagicMock, call
from NumberBaseball import Game

class NumberBaseballTest(unittest.TestCase):
    def assertGuessResult(self, correct_answer, guess_answer, right_chk_result):
        game = Game(correct_answer)
        game_chk_result = game.guess_checker(guess_answer)
        self.assertEqual(right_chk_result, game_chk_result)

    def test_guess_correct_answer_then_3S(self):
        self.assertGuessResult("369", "369", "3S")
        self.assertGuessResult("106", "106", "3S")

    def test_guess_all_wrong_answer_then_OUT(self):
        self.assertGuessResult("369", "145", "OUT")
        self.assertGuessResult("369", "145", "OUT")