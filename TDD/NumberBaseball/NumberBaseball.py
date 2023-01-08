import random

class Game:
    def __init__(self, correct_answer):
        if correct_answer:
            self.correct_anser = correct_answer
        else:
            self.correct_anser = random.sample(['0','1','2','3','4','5','6','7','8','9'],3)
            self.correct_anser = ''.join(self.correct_anser)

    def guess_checker(self, guess):
        if guess == self.correct_anser:
            return "3S"

        else:
            return f"test용 print : {self.correct_anser}"