import functions_declaration as fd

# PLEASE CHECK README.md FILE
# iF YOU WANT TO CHECK THE CODE OF THE FUNCTIONS, THEN PLEASE CHECK "FUNCTIONS_DECLARATION.PY" FILE

print("PART I")
print(fd.analyse_nba_game("NBA_game.txt"))
print("-------------------------------------------------------------------------------------------------------------------------------------")


dictionary_game_summary = fd.analyse_nba_game("NBA_game.txt")
print("PART II")
print(fd.print_nba_game_stats(dictionary_game_summary)[0])
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(fd.print_nba_game_stats(dictionary_game_summary)[1])