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
        self.assertGuessResult("106", "275", "OUT")

    def test_guess_just_one_right_number_right_location_then_1S(self):
        self.assertGuessResult("369", "382", "1S 0B")
        self.assertGuessResult("106", "709", "1S 0B")

    def test_guess_two_right_number_right_location_then_1S(self):
        self.assertGuessResult("369", "362", "2S 0B")
        self.assertGuessResult("106", "706", "2S 0B")

    def test_guess_one_right_number_but_wrong_location_then_1B(self):
        self.assertGuessResult("369", "238", "0S 1B")
        self.assertGuessResult("106", "079", "0S 1B")

    def test_guess_two_right_number_but_wrong_location_then_2B(self):
        self.assertGuessResult("369", "938", "0S 2B")
        self.assertGuessResult("106", "069", "0S 2B")

    def test_guess_three_right_number_but_wrong_location_then_3B(self):
        self.assertGuessResult("369", "936", "0S 3B")
        self.assertGuessResult("106", "061", "0S 3B")

    def test_guess_mix_strike_and_ball(self):
        self.assertGuessResult("369", "639", "1S 2B")
        self.assertGuessResult("106", "016", "1S 2B")
        self.assertGuessResult("369", "962", "1S 1B")
        self.assertGuessResult("106", "716", "1S 1B")

    def test_guess_more_or_less_than_3_length_then_length_error(self):
        self.assertGuessResult("369", "1", "LENGTH_ERROR")
        self.assertGuessResult("369", "12345678", "LENGTH_ERROR")

    def test_guess_duplicate_number_then_duplicate_error(self):
        self.assertGuessResult("369", "333", "DUPLICATE_ERROR")
        self.assertGuessResult("369", "110", "DUPLICATE_ERROR")