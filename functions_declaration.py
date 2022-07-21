#############################################################################################################################
# LIBRARIES
import pandas as pd
import numpy as np
import re

# PART I

# Function_name : 
# - analyse_nba_game
# Input : 
# - .txt File
# Output : 
# - dictionary 
# Description : 
# - Returns a dictionary with the summary of the game

def analyse_nba_game(play_by_play_moves):
        #############################################################################################################################
        # SETUP PART
        # VARIABLES INITIALIZATION
        player_stats = {"player_name": "",
                            "FG": 0, 
                            "FGA": 0, 
                            "FG%": 0, 
                            "3P": 0, 
                            "3PA": 0, 
                            "3P%": 0, 
                            "FT": 0, 
                            "FTA": 0, 
                            "FT%": 0, 
                            "ORB": 0, 
                            "DRB": 0, 
                            "TRB": 0, 
                            "AST": 0, 
                            "STL": 0, 
                            "BLK": 0, 
                            "TOV": 0, 
                            "PF": 0, 
                            "PTS": 0}
        players_list = []
        players_data = {}

        # THE TXT WILL CONVERT INTO A DATAFRAME
        df = pd.read_csv("NBA_game.txt", sep='|', engine='python')
        
        # THIS LOOP WILL SEARCH FOR ALL THE POSSIBLE PLAYER NAMES
        for x in df['DESCRIPTION']:
            players_list.extend(re.findall("[A-Z][.][ ][A-Z][a-z]*", x))  
        
        players_list = set(players_list).copy() 
        
        # THIS LOOP WILL CREATE THE TEMPLATE WHERE THE SCORES WILL BE STORED
        for x in players_list:
            player_stats["player_name"] = x
            players_data.update({x : player_stats.copy()})
            
        # HERE WILL CONVERT THE DICTIONARY INTO A DATAFRAME
        players_data_dataframe = pd.DataFrame(players_data)

        #############################################################################################################################
        # COUNTING PART

        moves_dictionary = {
            "FG" : "makes 2-pt",
            "FGA" : "misses 2-pt",
            "3P" : "makes 3-pt jump shot",
            "3PA" : "misses 3-pt jump shot",
            "FT" : "makes free throw",
            "FTA" : "misses free throw",
            "ORB" : "offensive rebound by",
            "DRB" : "defensive rebound by",
            "AST" : "assist by",
            "STL" : "steal by",
            "BLK" : "block by",
            "TOV" : "turnover by",
            "PF" : "foul by"
        }
        
        
        for x in players_list:
            for y in df['DESCRIPTION']:
             if x in y:
                # ACTIVE ACTIONS
                
                    # COUNTING FIELD GOAL
                if (x.lower() + " " + moves_dictionary["FG"]) in y.lower():
                    players_data_dataframe[x]["FG"] += 1
        
                    # COUNTING FIELD GOAL ATTEMPTED
                if (x.lower() + " " + moves_dictionary["FGA"]) in y.lower():
                    players_data_dataframe[x]["FGA"] += 1
        
                    # COUNTING 3 POINTS
                if (x.lower() + " " + moves_dictionary["3P"]) in y.lower():
                    players_data_dataframe[x]["3P"] += 1
        
                    # COUNTING 3 POINTS ATTEMPTED
                if (x.lower() + " " + moves_dictionary["3PA"]) in y.lower():
                    players_data_dataframe[x]["3PA"] += 1
        
                    # COUNTING FREE THROWS
                if (x.lower() + " " + moves_dictionary["FT"]) in y.lower():
                    players_data_dataframe[x]["FT"] += 1
        
                    # COUNTING FREE THROWS ATTEMPTED
                if (x.lower() + " " + moves_dictionary["FTA"]) in y.lower():
                    players_data_dataframe[x]["FTA"] += 1
        
                # PASSIVE ACTIONS
        
                    # COUNTING OFFENSIVE REBOUND
                if (moves_dictionary["ORB"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["ORB"] += 1
        
                    # COUNTING DEFFENSIVE REBOUND
                if (moves_dictionary["DRB"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["DRB"] += 1
        
                    # COUNTING ASSISTANCE
                if (moves_dictionary["AST"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["AST"] += 1
        
                    # COUNTING STEAL
                if (moves_dictionary["STL"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["STL"] += 1
        
                    # COUNTING BLOCK
                if (moves_dictionary["BLK"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["BLK"] += 1
        
                    # COUNTING TURNOVER
                if (moves_dictionary["TOV"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["TOV"] += 1
        
                    # COUNTING PERSONAL FOULS
                if (moves_dictionary["PF"] + " " + x.lower()) in y.lower():
                    players_data_dataframe[x]["PF"] += 1
        
            # CALCULATING FIELD GOAL PORCENTAGE
            if players_data_dataframe[x]["FGA"] > 0:
                players_data_dataframe[x]["FG%"] = players_data_dataframe[x]["FG"] / players_data_dataframe[x]["FGA"]
        
            # CALCULATING 3 POINTS PORCENTAGE
            if players_data_dataframe[x]["3PA"] > 0:
                players_data_dataframe[x]["3P%"] = players_data_dataframe[x]["3P"] / players_data_dataframe[x]["3PA"]
        
            # CALCULATING FREE THROWS PORCENTAGE
            if players_data_dataframe[x]["FTA"] > 0:
                players_data_dataframe[x]["FT%"] = players_data_dataframe[x]["FT"] / players_data_dataframe[x]["FTA"]
        
            # CALCULATING TOTAL POINTS
            players_data_dataframe[x]["PTS"] = players_data_dataframe[x]["FG"] + players_data_dataframe[x]["3P"]*3 + players_data_dataframe[x]["FT"]
        
        players_data = players_data_dataframe.to_dict()

        # OUTPUT:
        # players_data : dictionary
        # players_data_dataframe : DataFrame

        #############################################################################################################################
        # SORTING PLAYERS PART

        team1 = {
            "name" : df["HOME_TEAM"][0]
        }
        
        team2 = {
            "name" : df["AWAY_TEAM"][0]
        }
        
        
        index = 0
        for x in players_list:
            for y in df["DESCRIPTION"]:
                if x in y:
                    if df["RELEVANT_TEAM"][index] == df["HOME_TEAM"][index]:
                        team1.update({x : players_data[x]})
                        break
                
                    elif df["RELEVANT_TEAM"][index] == df["AWAY_TEAM"][index]:
                        team2.update({x : players_data[x]})
                        break
                index += 1
            index = 0
        
        
        output_dictionary = {
                "home_team": team1, 
                "away_team": team2
            }

        # OUTPUT:
        # output_dictionary : dictionary

        
        return output_dictionary

#############################################################################################################################
# PART II

# Function_name : 
# - print_nba_game_stats
# Input : 
# - dictionary
# Output : 
# - dataframe - home team
# - dataframe - away team
# Description :
# - Returns two dataframes with summary of each team

def print_nba_game_stats(team_dict):

    #############################################################################################################################
    # SORTING PLAYERS PART

    team1_list = []
    team1_stats = []

    team2_list = []
    team2_stats = []

    columns_list = [
           "Players",
           "FG",
           "FGA",	
           "FG%", 
           "3P",	
           "3PA",	
           "3P%",	
           "FT",	
           "FTA",	
           "FT%",	
           "ORB",	
           "DRB",	
           "TRB",	
           "AST",
           "STL",
           "BLK",
           "TOV",
           "PF",
           "PTS"]

    for x in team_dict["home_team"]:
        team1_list.append(x)

    team1_list.pop(0)


    for x in team1_list:
  
        list_temp = [team_dict["home_team"][x]["player_name"],
                 team_dict["home_team"][x]["FG"],
                 team_dict["home_team"][x]["FGA"],
                 team_dict["home_team"][x]["FG%"],
                 team_dict["home_team"][x]["3P"],
                 team_dict["home_team"][x]["3PA"],
                 team_dict["home_team"][x]["3P%"],
                 team_dict["home_team"][x]["FT"],
                 team_dict["home_team"][x]["FTA"],
                 team_dict["home_team"][x]["FT%"],
                 team_dict["home_team"][x]["ORB"],
                 team_dict["home_team"][x]["DRB"],
                 team_dict["home_team"][x]["TRB"],
                 team_dict["home_team"][x]["AST"],
                 team_dict["home_team"][x]["STL"],
                 team_dict["home_team"][x]["BLK"],
                 team_dict["home_team"][x]["TOV"],
                 team_dict["home_team"][x]["PF"],
                 team_dict["home_team"][x]["PTS"]]

        team1_stats.append(list_temp.copy())

    for x in team_dict["away_team"]:
        team2_list.append(x)

    team2_list.pop(0)

    for x in team2_list:
  
        list_temp = [team_dict["away_team"][x]["player_name"],
                 team_dict["away_team"][x]["FG"],
                 team_dict["away_team"][x]["FGA"],
                 team_dict["away_team"][x]["FG%"],
                 team_dict["away_team"][x]["3P"],
                 team_dict["away_team"][x]["3PA"],
                 team_dict["away_team"][x]["3P%"],
                 team_dict["away_team"][x]["FT"],
                 team_dict["away_team"][x]["FTA"],
                 team_dict["away_team"][x]["FT%"],
                 team_dict["away_team"][x]["ORB"],
                 team_dict["away_team"][x]["DRB"],
                 team_dict["away_team"][x]["TRB"],
                 team_dict["away_team"][x]["AST"],
                 team_dict["away_team"][x]["STL"],
                 team_dict["away_team"][x]["BLK"],
                 team_dict["away_team"][x]["TOV"],
                 team_dict["away_team"][x]["PF"],
                 team_dict["away_team"][x]["PTS"]]

        team2_stats.append(list_temp.copy())


    df1 = pd.DataFrame(data=np.array(team1_stats), columns=columns_list)
    df2 = pd.DataFrame(data=np.array(team2_stats), columns=columns_list)

    return df1, df2








