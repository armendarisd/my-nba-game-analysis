import functions_declaration as fd



# PART I - PRINT DICTIONARY
print('PART I')
play_by_play_moves = 'NBA_game.txt'
print(fd.analyse_nba_game(play_by_play_moves))

dictionary_game_summary = fd.analyse_nba_game(play_by_play_moves)

# PART II - PRINT DATAFRAME

print('PART II')
print('Home team')
print(fd.print_nba_game_stats(dictionary_game_summary)[0])
print('Away Team')
print(fd.print_nba_game_stats(dictionary_game_summary)[1])
