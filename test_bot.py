import pytest
########################
## Import Other Files ##
########################

from player_bot import Player_Bot
from game_jb import Game

##################
## Test Imports ##
##################

def test_game():
  assert Game()

def test_bot():
  assert Player_Bot()

#####################
## Pytest Features ##
#####################

@pytest.fixture()
def game():
  return Game()

@pytest.fixture()
def bot():
  return Player_Bot()

##############################
## Test Bot Best Move Logic ##
##############################

@pytest.mark.parametrize("roll, output",[
  ([1], '1'),
  ([1,1], '11'),
  ([1,1,1], '111'),
  ([1,1,1,1], '1111'),
  ([1,1,1,1,1], '11111'),
  ([1,1,1,1,1,1], '111111'),
  ([2,2,3,3,6,6], '223366'),
  ([2,2,2,6,6,6], '222666'),
  ([1,1,2,3,5,6], '1'),
  ([1,1,1,1,5,5], '111155'),
  ([1,5,1,1,5,1], '151151'),
  ([1,5,1,1,5], '15115'),
  ([6,6,6,1], '6661'),
  ([6,6,6,1,2,2], '666'),
  ([6,6,6,1,1,2], '66611'),
  ([5,5,1,1], '5511'),
  ([5,6], '5'),
  ([2,2,2,3,4,6], ''),
])
def test_bot_move(bot, roll, output):
  assert output == bot.selected_dice(roll)

