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

  def __init__(self, _print=hack_print , _input=hack_input):
    """Currently just sets the print and input to the default methods"""
    self._player1_score = 0
    self._player2_score = 0


    self._print=_print
    self._input=_input


  def play(self):
    """Controls the main game loop. That includes starting and stopping the game based on user input"""
    valid_inputs = {'y','yes','ok','okay'}
    self._print('Welcome to Game of Greed')
    player_input = self._input("Wanna play?")
    if player_input.lower() in valid_inputs:
      self._print('Great! Check back tomorrow :D')
    else:
      self._print('OK. Maybe another time')


  def turn(self):
    bank = 0
    saved_dice = []

    end = False
    while not end:

      roll = self.roll_dice(6 - len(saved_dice))
      print(roll)
      roll_score = self.calculate_score(roll)

      # Break from the loop and end the turn
      if roll_score == 0:
        print('Roll 0 end Turn')
        bank = 0
        end = True
        continue

        ########################################
        ## Beyond This Point There be Dragons ##
        ##            Turn Back Now           ##
        ########################################

      # Let the player decide their actions
      exit = False
      while not exit:
        user_input = input("What would you like to do? ")
        if re.match(r"[Hh]elp", user_input):
          print('\nBank Points: `bank`')
          print('Save Dice:   `save #,count`')
          print('Roll:        `roll` *Can only be done after a save*\n')
        elif re.match(r"[Bb]ank", user_input):
          bank += roll_score
          exit = True
          end = True
        elif re.match(r'[Ss]ave', user_input):
          if (re.match(r'save\s[1-6],[1-6]', user_input)):
            num = re.findall(r"[1-6]", user_input)
            count = Counter(roll)
            position = int(num[1])
            value = int(num[0])
            if count[position] >= value:

              print(count[position])
              count[position] -= value
              print(count[position])

              ## Need to make sure the removed values score points ##
          else:
            print('Invalid Save Format: `save [count],[num]')
        elif re.match(r"[Rr]oll", user_input):
          exit = True
        else:
          print('Invalid Input\nType \'help\' for help')

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
      elif key == 1:
        sum += count[key] * 10
      elif key == 5:
        sum += count[key] * 50

      if key == 1:
        # The key of one will always be first in the range(1-6) of dice is kept so thos won't effect the overall score
        sum *= 10

      total += sum
    return total


  def roll_dice(self, times = 1):
    rolls = []
    for x in range(0, times):
      rolls.append(randint(1,6))
    return rolls

  def testing_console(self, print_func=None, input_func=None):
    """***TESTING ONLY*** It is designed to take in override functions for both the print and input functions. Then run the play method"""
    if print_func:
      self._print = print_func
    if input_func:
      self._input = input_func
    self.play()


if __name__ == "__main__":

    game = Game()

    print(game.turn())
