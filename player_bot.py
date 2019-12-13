import re
from game_jb import Game
from collections import Counter

class Player_Bot:
  """A bot program that can be used in place of a play in the place of a player"""
  def __init__(self):
    self.name = "Definitely Doen't Cheat"
    self.last_roll = []
    self.dice_remain = 6
    self.current_bank = 0


  def _print(self, *args):
    """The replacement version of the _pring for the game class"""
    print(args[0])
    if re.search(r"\[([1-6],?\s?){1,6}\]", args[0]):
      self.last_roll = tuple( int(num) for num in re.findall(r"[1-6]", args[0]) )
    elif re.search(r"[Bb]ank", args[0]):
      self.current_bank = int(re.sub(r"[^0-9]", '', args[0]))


  def _input(self, *args):
    """The replacement version of the _input for the game class"""
    if args[0] == 'Enter dice to keep: ':
      return self.selected_dice(self.last_roll)
    elif re.search(r'Roll again\?', args[0]):
      return self.roll_again()
    return 'y'


  def selected_dice(self, roll):
    """Allow the bot to select the best dice combo and return it as a valid game input"""
    self.dice_remain = len(roll)
    count = Counter(roll)
    if self.six_dice_roll(count, roll):
      return re.sub(r"[^1-6]", '',str(roll))

    return self._handle_sets(count)


  def _handle_sets(self, count):
    """Checks for possible sets of and if there are only a few dice remaining try to get any extra points"""

    for key in count.keys():
      if count[key] > 2:

        output = ''

        for _ in range(count[key]):
          if key == 2:
            continue
          self.dice_remain -= 1
          output += str(key)

        if count[1] > 0 and self.dice_remain - count[1] <= 1 and not key == 1:
          for _ in range(count[1]):
            self.dice_remain -= 1
            output += '1'

        if count[5] > 0 and self.dice_remain <= 2 and not key == 5:
          self.dice_remain -= 1
          output += '5'

        return output

    return self._return_remainders(count)


  def _return_remainders(self, count):
    """If there were no other points claim either a 1 or 5 to be able to roll again"""
    print(self.last_roll)
    if count[1] > 0:
      self.dice_remain -= 1
      return '1'
    else:
      self.dice_remain -= 1
      return '5'

  def six_dice_roll(self, count, roll):
    """See if the last roll was a combination of dice that is entirely scoring combinations"""
    if count[1] + count[5] == self.dice_remain:
      return True
    if len(roll) == 6:
      if len(count) == 3 and count.most_common(3)[2][1] == 2:
        return True
      if len(count) == 6:
        return True
      if len(count) == 2 and count.most_common(2)[0][1] == 3:
        return True
      if len(count) == 1:
        return True
    return False


  def roll_again(self):
    """Decide if the bot should try to roll again"""

    if self.dice_remain == 0:
      self.dice_remain = 6
    if self.dice_remain == 6:
      return 'y'
    elif self.current_bank >= 2000:
      return 'n'
    elif self.current_bank >= 800 and self.dice_remain < 5:
      return 'n'
    elif self.current_bank <= 200:
      return 'y'
    elif self.dice_remain > 3:
      return 'y'
    return 'n'

if __name__ == "__main__":
  bot = Player_Bot()
  game = Game(bot._print, bot._input)
  games = 1000

  high_score = 0
  total_score = 0
  low_score = 10000

  for _ in range(games):
    round_score = int(game.play())

    total_score += round_score
    high_score = round_score if round_score > high_score else high_score
    low_score = round_score if round_score < low_score else low_score

  print('Average Score: ' + str(total_score/games))
  print('Highest Score: ' + str(high_score))
  print('Lowest Score:  ' + str(low_score))
