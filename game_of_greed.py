from collections import Counter
from random import randint
import re

# Needed to subvert the problems with reassigning the print method.
def hack_print(msg):
    print(msg)

def hack_input(msg):
  return input(msg)

class Game:
  """The class that controlls most aspects of the game from the basics of the game loop to the score counting"""
  _valid_yes = {'y','yes','ok','okay','sure','affirmative'}
  _valid_no = {'n','no','nope','none','naw'}

  def __init__(self, _print=hack_print , _input=hack_input):
    """Currently just sets the print and input to the default methods"""
    self._player1_score = 0
    self._player2_score = 0


    self._print=_print
    self._input=_input


  def play(self):
    """Controls the main game loop. That includes starting and stopping the game based on user input"""
    self._print('Welcome to Game of Greed')
    player_input = self._input("Wanna play?")
    if player_input.lower() in self._valid_yes:
      turns = 0
      while turns < 10:
        self._print('Player 1 it\'s your turn!')
        self._player1_score = self.turn()
        turns += 1
      self._print('Your Final Score is:' + str(self._player1_score))
    else:
      self._print('OK. Maybe another time')


  def turn(self):
    bank = 0
    saved_dice = 0

    end_turn = False
    while not end_turn:

      roll = self.roll_dice(6 - saved_dice % 6)

      roll_score = self.calculate_score(roll)

      # Break from the loop and end the turn
      if roll_score == 0:
        self._print('Zilch, Your Turn Is Over')
        bank = 0
        end_turn = True
        continue

        ########################################
        ## Beyond This Point There be Dragons ##
        ##            Turn Back Now           ##
        ########################################
        # I'm keeping this in. Period.

      valid_save=False
      while not valid_save:
        self._print('You Rolled: ' + str(roll))
        self._print('Your Current Bank is: ' + str(bank))
        response = input('Enter dice to keep: ')

        if re.search(r"[1-6]{1,6}", response):

          saved = tuple( int(num) for num in re.findall(r"[1-6]", response) )
          count = Counter(saved)
          count_list = list(count.elements())
          bad_entry = False
          if bad_entry:
            self._print("Bad Save Values")
            continue
          saved_dice += len(saved)
          bank += self.calculate_score(count_list)
          valid_save = True
        else:
          self._print("Bad Save Values")


      response = self._input('Roll again? ')
      if response.lower() in self._valid_no:
        end_turn = True

    return bank


  def calculate_score(self, dice):
    """Takes in a list of numbers in the range of 1 to 6 inclusive and calcuates a score based on the given inputs"""
    count = Counter(dice[:6])

    #Return Score Based on special conditions
    if count[1] == 2 and count[5] == 4:
      return 2000

    if len(count) == 6:
      return 1500

    #A little more cluttered but effectively the fastest solution I can think of. (.most_common returns a 2d list.)
    if len(count) == 3 and count.most_common(3)[2][1] == 2:
      return 1500

    # Handle other sum cases. Since 1 is run first
    total = 0

    for key in count:
      sum = 0
      if count[key] > 2:
        sum += ((count[key]-2)*100)*key
      elif key == 1 or key == 5:
        sum += count[key] * 10 * key

      if key == 1:
        # The key of one will always be first in the range(1-6) of dice is kept so thos won't effect the overall score
        sum *= 10

      total += sum
    return total


  def roll_dice(self, times = 1):
    return [randint(1,6) for _ in range(times)]

  def testing_console(self, print_func=None, input_func=None):
    """***TESTING ONLY*** It is designed to take in override functions for both the print and input functions. Then run the play method"""
    if print_func:
      self._print = print_func
    if input_func:
      self._input = input_func
    self.play()

  def testing_flow(self):
    """***TESTING ONLY***"""
    pass


if __name__ == "__main__":

    game = Game()

    game.play()
