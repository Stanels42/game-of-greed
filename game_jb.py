""""Game Module Docstring"""

import random
from collections import Counter


class CheatingScoundrelError(ValueError):
    pass

def hack_print(msg):
    print(msg)

def hack_input(msg):
  var = input(msg)
  return var

class Game:
    """Game of Greed Class"""

    def __init__(self, print_func=hack_print, input_func=hack_input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.num_rounds = 10

    def play(self, num_rounds=10):

        self.num_rounds = num_rounds

        self._print('Welcome to Game of Greed')

        response = self._input('Wanna play? ')

        if response == 'y':
            self._start()
        else:
            self._print('OK. Maybe later')

        return self.score


    def _start(self):

        self.score = 0

        round_num = 1

        for _ in range(1, self.num_rounds + 1):
            round_score = self._do_round()

            self._print(
                'You banked ' + str(round_score) + ' points in round ' + str (round_num))

            self.score += round_score

            round_num += 1

            self._print(str('You have ' + str(self.score) + ' points total'))

        self._print('Thanks for playing!')

    def _do_round(self):
        num_dice = 6

        score = 0

        while(True):
            self._print(str('Rolling ' + str(num_dice) + ' dice'))

            roll = self._do_roll(num_dice)

            zilch_check_score = self.calculate_score(roll)

            self._print(str('You rolled ' + str(roll)))

            if zilch_check_score == 0:
                self._print('Oh noes! Zilch')
                return 0

            keepers = self.validate_roll(roll)

            # TODO: handle non scoring but mysteriously used dice
            num_dice -= len(keepers)

            score += self.calculate_score(keepers)

            self._print(str('You can bank ' + str(score) + ' points or try for more'))

            if num_dice == 0:
                num_dice = 6

            self._print(str('You have '+ str(num_dice) + ' dice remaining'))

            roll_again_response = self._input('Roll again? ')

            if not roll_again_response == 'y':
                break

        return score

    def validate_roll(self, roll):

        while True:

            keep_response = self._input('Enter dice to keep: ')

            keepers = tuple(int(char) for char in keep_response)

            if self.validate(roll, keepers):
                return keepers
            else:
                self._print('No way pal')
                self._print(roll)

    def validate(self, roll, keepers):

        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        return len(keepers_counter - roll_counter) == 0

    def calculate_score(self, dice):

        score = 0

        dice_counter = Counter(dice)

        ones_used = False
        fives_used = False

        for key in dice_counter:

            count = dice_counter[key]

            if count >= 3:
                score += key * 100

                if key == 1:
                    score = 1000
                    ones_used = True
                elif key == 5:
                    fives_used = True

            if count >= 4:
                if key == 1:
                    score += 1000
                else:
                    score += key * 100

            if count >= 5:
                if key == 1:
                    score += 1000
                else:
                    score += key * 100

            if count == 6:
                if key == 1:
                    score += 1000
                else:
                    score += key * 100

        # must be a straight
        if len(dice_counter) == 6:
            score = 1500
            ones_used = True
            fives_used = True

        # must be 3 pairs
        if len(dice_counter) == 3 and dice_counter.most_common()[2][1] == 2:
            ones_used = True
            fives_used = True
            score = 1500

        if not ones_used:
            score += dice_counter[1] * 100

        if not fives_used:
            score += dice_counter[5] * 50

        return score

    def _do_roll(self, num_dice):
        """simulate dice roll for given number of dice"""
        return [random.randint(1, 6) for _ in range(num_dice)]


if __name__ == "__main__":
    game = Game()
    game.play()
