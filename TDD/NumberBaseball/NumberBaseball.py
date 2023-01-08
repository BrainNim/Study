import random

class Game:
    def __init__(self, correct_answer):
        if correct_answer:
            self.correct_anser = correct_answer
        else:
            self.correct_anser = random.sample(['0','1','2','3','4','5','6','7','8','9'],3)
            self.correct_anser = ''.join(self.correct_anser)

    def guess_checker(self, guess):
        # if guess == self.correct_anser:
        #     return "3S"

        # out check
        out_checker = 0
        for n in guess:
            if n not in self.correct_anser:
                out_checker += 1

        if out_checker == 3:
            return "OUT"

        # strike check
        strike_checker = 0
        for i in range(3):  # 3자리 수 숫자
            if guess[i] == self.correct_anser[i]:
                strike_checker += 1

        return f"{strike_checker}S"