from collections import Counter

class Game:
  """The class that controlls most aspects of the game from the basics of the game loop to the score counting"""

  def __init__(self):
    """Currently just sets the print and input to the default methods"""
    self._print=self.hack_print
    self._input=self.hack_input


  def play(self):
    """Controls the main game loop. That includes starting and stopping the game based on user input"""
    valid_inputs = {'y','yes','ok','okay'}
    self._print("Welcome to the Game of Greed")
    player_input = self._input("Do you Wanna Play? (Y/N)")
    if player_input.lower() in valid_inputs:
      self._print('Come back later, Current WIP')
    else:
      self._print('Bye Then...')


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

      if count[key] > 2:
        total += ((count[key]-2)*100)*key
      elif key == 1:
        total += count[key] * 10
      elif key == 5:
        total += count[key] * 50

      if key == 1:
        # The key of one will always be first in the range(1-6) of dice is kept so thos won't effect the overall score
        total *= 10

    return total


  def testing_console(self, print_func=None, input_func=None):
    """***TESTING ONLY*** It is designed to take in override functions for both the print and input functions. Then run the play method"""
    if print_func:
      self._print = print_func
    if input_func:
      self._input = input_func
    self.play()


  @staticmethod
  def hack_print(msg):
      print(msg)


  @staticmethod
  def hack_input(msg):
    return input(msg)



if __name__ == "__main__":

    game = Game()

    game.play()
