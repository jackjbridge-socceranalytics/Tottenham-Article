# coding=utf-8

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read in the data sets for the last 4 seasons
stats2019_2020 = pd.read_csv('2019-2020.csv')
stats2018_2019 = pd.read_csv('2018-2019.csv')
stats2017_2018 = pd.read_csv('2017-2018.csv')
stats2016_2017 = pd.read_csv('2016-2017.csv')

# Calculate the new goals_above_expected stat for each season
stats2019_2020['goals_above_expected1'] = stats2019_2020['npg'] - stats2019_2020['npxG']
stats2018_2019['goals_above_expected2'] = stats2018_2019['npg'] - stats2018_2019['npxG']
stats2017_2018['goals_above_expected3'] = stats2017_2018['npg'] - stats2017_2018['npxG']
stats2016_2017['goals_above_expected4'] = stats2016_2017['npg'] - stats2016_2017['npxG']

# Filter each season to only get the premier league players
stats2019_2020epl = stats2019_2020[stats2019_2020['league'] =='EPL']
stats2018_2019epl = stats2018_2019[stats2018_2019['league'] =='EPL']
stats2017_2018epl = stats2017_2018[stats2017_2018['league'] =='EPL']
stats2016_2017epl = stats2016_2017[stats2016_2017['league'] =='EPL']

# merge all the tables together on table name, so we can calculate total goals above expected for the last 4 seasons
table_merged_EPL1 = pd.merge(stats2019_2020epl, stats2018_2019epl, on='player_name')
table_merged_EPL2 = pd.merge(table_merged_EPL1, stats2017_2018epl, on='player_name')
final_tableEPL = pd.merge(table_merged_EPL2, stats2016_2017epl, on='player_name')

# Calculate total goals above expected for the last 4 seasons, then sort and grab the top 8 so we can display in a graph
final_tableEPL['total_GAE'] = final_tableEPL['goals_above_expected1'] + final_tableEPL['goals_above_expected2'] + final_tableEPL['goals_above_expected3'] + final_tableEPL['goals_above_expected4']
final_EPL_sorted = final_tableEPL.sort_values(by='total_GAE', ascending=False).head(n=8)

# Grab just the players and the total goals above expected so we can make a bar graph with those two
players = final_EPL_sorted['player_name']
total_GAE = final_EPL_sorted['total_GAE']
# Pass the x and y cordinates of the bars to the
# function. The label argument gives a label to the data.
barlist = plt.bar(players,total_GAE)

# Hard-coding the colors for each bar for now, so we can change the bars to represent the color for each team the players play for
barlist[0].set_color('navy')
barlist[1].set_color('navy')
barlist[2].set_color('red')
barlist[3].set_color('blue')
barlist[4].set_color('red')
barlist[5].set_color('lightskyblue')
barlist[6].set_color('red')
barlist[7].set_color('lightskyblue')

# The following commands add labels to our figure.
plt.xlabel('Player Name')
plt.ylabel('Total Goals Above Expected')
plt.title('Total Goals Above Expected Over the Last 4 Premier League Seasons')

plt.show()