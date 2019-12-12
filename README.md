
# Project Name

**Author**: Chris Stanley
**Version**: 1.0.0

## Overview
The goal of this application is to recreate the dice game known as *The Game of Greed* in the terminal using python.

Day 1: Create a method that acceretly sums up the score based on a list of 'Dice Rolls' and reuns a series of tests on the outputs to make sure they function. The other half was to create a user input field that asks if they wanna start the game. This also has a set of coresponding tests relating to it's function.

Day 1.5/2: Work on a method for controling the turns. Allows the user to save dice, bank current points or reroll remaing dice. (Incompleate)

Day 3: Made an improved version of the save dice controls. Simplified the input strean to make it easier to handle. Currently the function can take in valid scoring options but doesn't compare input to rooled dice. In major need of refactoring and tests.

## Getting Started
Currently the game can be run with the command `python game_of_greed.py` in the terminal. Currently the user will only be met with a single prompt before the game ends.

## Architecture
The counter class needed to be imported from collections. That class was used when tallying up the total dice rolls for each roll. The structure currently only has a The ability to score dice rolls not to make the rolls themselves.

## APIs
Uses Counter, randint and re
Play: Time: `O`<br>
Calcualte_Score: Time: `O`<br>
Turn: Eficencey Unknown (User Controlled)

## Change Log
V 0.1 4:47pm 12/09/19 Compleated the frature tasks for finding score from a set of dice rolls<br>
V 0.2 6:25pm 12/09/19 Compleated the tasks for testing the input and output on game start<br>
V 1.0 6:25pm 12/09/19 Part one has been compleated<br>
V 1.1 2:30pm 12/10/19 Fixed some testing and workding mistakes<br>
V 1.2 9:00om 12/10/19 Basic user function on the turns albeit incompleate.<br>
V 1.3 7:00pm 12/11/19 Reworked the controls for the user to make the input and output more intuitive<br>
