######################
## Import Libraries ##
######################

import pytest

####################
## Import Classes ##
####################

from game_of_greed import Game

#####################
## Test Game Start ##
#####################

def test_start_game(game):
  prints = ["Welcome to Game of Greed", 'Great! Check back tomorrow :D']
  prompts = ["Wanna play?"]
  response = ['Yes']

  run_io(game, prints, prompts, response)


def test_dont_start(game):
  prints = ["Welcome to Game of Greed", 'OK. Maybe another time']
  prompts = ["Wanna play?"]
  response = ['No']

  run_io(game, prints, prompts, response)


def run_io(game, prints, prompts, response):

  def printing(message):
    assert message == prints.pop(0)

  def inputs(message):
    assert message == prompts.pop(0)
    return response.pop(0)

  game.testing_console(printing, inputs)


#################
## Test Scores ##
#################

@pytest.mark.parametrize("roll, expected",[
  ([], 0),
  ([2,3], 0),
  ([2,2,3,3,4,6], 0)
])
def test_zilch(game, roll, expected):
  assert expected == game.calculate_score(roll)


@pytest.mark.parametrize("roll, expected",[
  ([1], 100),
  ([1,1], 200),
  ([1,1,1], 1000),
  ([1,1,1,1], 2000),
  ([1,1,1,1,1], 3000),
  ([1,1,1,1,1,1], 4000)
])
def test_ones(game, roll, expected):
  assert expected == game.calculate_score(roll)

@pytest.mark.parametrize("roll, expected",[
  ([2], 0),
  ([2,2], 0),
  ([2,2,2], 200),
  ([2,2,2,2], 400),
  ([2,2,2,2,2], 600),
  ([2,2,2,2,2,2], 800),
  ])
def test_twos(game, roll, expected):
  assert expected == game.calculate_score(roll)


def test_threes(game):
  assert 0 == game.calculate_score([3])
  assert 0 == game.calculate_score([3,3])
  assert 300 == game.calculate_score([3,3,3])
  assert 400 == game.calculate_score([3,1,3,3,4,6])
  assert 600 == game.calculate_score([3,3,3,3,4,6])
  assert 900 == game.calculate_score([3,3,3,3,3])
  assert 1200 == game.calculate_score([3,3,3,3,3,3])

def test_fours(game):
  assert 0 == game.calculate_score([4])
  assert 0 == game.calculate_score([4,4])
  assert 400 == game.calculate_score([4,4,4])
  assert 800 == game.calculate_score([4,4,4,4])
  assert 1200 == game.calculate_score([4,4,4,4,4])
  assert 1600 == game.calculate_score([4,4,4,4,4,4])

def test_fives(game):
  assert 50 == game.calculate_score([5])
  assert 100 == game.calculate_score([5,5])

def test_sixes(game):
  assert 0 == game.calculate_score([6])
  assert 0 == game.calculate_score([6,6])
  assert 600 == game.calculate_score([6,6,6])
  assert 1200 == game.calculate_score([6,6,6,6])
  assert 1800 == game.calculate_score([6,6,6,6,6])
  assert 2400 == game.calculate_score([6,6,6,6,6,6])

def test_three_pairs(game):
  assert 1500 == game.calculate_score([3,3,4,4,6,6])
  assert 1500 == game.calculate_score([3,3,4,4,5,5])
  assert 1500 == game.calculate_score([1,2,3,2,3,1])
  assert 1500 == game.calculate_score([1,2,5,2,1,5])
  assert not 1500 == game.calculate_score([1,1,2,2,3,4,3]) #The last 3 should be trimmed before the dataset is made
  assert not 1500 == game.calculate_score([1,1,2,2,3]) #Only 5 values entered

def test_two_trios(game):
  assert 1200 == game.calculate_score([1,1,1,2,2,2])
  assert 800 == game.calculate_score([6,6,6,2,2,2])
  assert 700 == game.calculate_score([3,4,3,4,4,3])
  assert 900 == game.calculate_score([5,4,5,4,4,5])

def test_grand(game):
  assert 2000 == game.calculate_score([5,5,5,5,1,1])
  assert 2000 == game.calculate_score([1,5,5,5,1,5])

def test_leftover_ones(game):
  assert 100 == game.calculate_score([1,2,3,4,6,4])
  assert 200 == game.calculate_score([1,3,3,1,6,4])
  assert 500 == game.calculate_score([1,2,4,4,6,4])

def test_leftover_fives(game):
  assert 50 == game.calculate_score([5,3,3,2,2,6])
  assert 100 == game.calculate_score([5,5,3,2,2,6])
  assert 200 == game.calculate_score([5,2,3,5,1,6])

###############
## Roll Dice ##
###############

def test_dice_roll(game):
  assert 7 not in range(1,7)
  assert 0 not in range(1,7)
  assert game.roll_dice()[0] in range(1,7)
  assert game.roll_dice()[0] in range(1,7)

#######################
## Make Game Fixture ##
#######################

@pytest.fixture()
def game():
  return Game()
