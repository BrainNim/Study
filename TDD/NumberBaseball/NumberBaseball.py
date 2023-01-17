import random

class Game:
    def __init__(self, correct_answer=None):
        if correct_answer:
            self.correct_anser = correct_answer
        else:
            self.correct_anser = random.sample(['0','1','2','3','4','5','6','7','8','9'],3)
            self.correct_anser = ''.join(self.correct_anser)

    def guess_checker(self, guess):
        if len(guess) != 3:
            return "LENGTH_ERROR"

        if len(set(guess)) !=3:
            return "DUPLICATE_ERROR"

        if guess == self.correct_anser:
            return "3S"

        # out/ball check
        out_checker = 0
        ball_checker = 0
        for n in guess:
            if n in self.correct_anser:
                ball_checker += 1
            else:
                out_checker += 1

        if out_checker == 3:
            return "OUT"


        # strike check
        strike_checker = 0
        for i in range(3):  # 3자리 수 숫자
            if guess[i] == self.correct_anser[i]:
                strike_checker += 1

        # revise ball check
        ball_checker -= strike_checker

        return f"{strike_checker}S {ball_checker}B"


if __name__ == '__main__':
    game = Game()

    result = ""
    count = 0
    while result != "3S":
        guess = input("3자리 숫자입력 : ")
        result = game.guess_checker(guess)
        if result == "LENGTH_ERROR":
            print("입력숫자 에러!! 세자리 숫자만 입력해 주세요")
            continue
        elif result == "DUPLICATE_ERROR":
            print("입력숫자 에러!! 동일한 숫자를 중복으로 입력할 수 없습니다")
            continue

        print(result)
        count += 1


    print(f"축하합니다. 정답은 {game.correct_anser} 였습니다")
    print(f"{count}번 만에 정답을 맞췄습니다!")