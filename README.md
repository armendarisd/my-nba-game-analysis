# Welcome to My Nba Game Analysis
***

## Task

PART I
As input one receives a CSV which has all the plays on a Basketball game. One should return a dictionary where one gives all the stats of the game of each player.

PART II
After returning the dictionary, then one should organize a table where for each team
## Description

I use Pandas to have some dataframes to make it easier

## Installation

Type python my_nba_game_analysis.py

## Usage


 IMPORTANT NOTES

 PART I
 The function analyse_nba_game() receives a .txt file. The file is uploaded in the same folder where the script .py is.
 If you want to try with another game information. 
 Please create another .txt file starting with the following header:

 Example
 PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
 1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)
 1|703.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by P. George (bad pass)
 1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)
 1|673.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Adams misses 2-pt jump shot from 12 ft
 1|671.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Offensive rebound by D. Schröder

 After doing it, then you can put the name of the .txt file as parameter for the function

 #########################################################################################

 PART II
 The  function print_nba_game_stats() receives the dictionary from the first part. That dictionary is stored in the variable "dictionary_game_summary".
 The function return two values. One for the home team the another one for the away team. You should use indexes to specify which value you want to show

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar Silicon Valley</a></i></span>
<span><img alt='Qwasar Silicon Valley Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
