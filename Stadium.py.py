#######################################################
# This script is used to analyse the data from a file
# The data used is IPL Matches data set from 2008 to 2020
# The stadium wise basic statistics have been displayed
# Author: 
# Created at: 22-10-2021
# Last Modified at: 26-10-2021
####################################################################################

import pandas as pd

#reading data from the csv file
df = pd.read_csv('IPL Matches 2008-2020.csv') 

stadium = df['venue'] #selecting the column named venue
stadium = set(stadium) #changing the type to 'set' to avoid the duplicates

for i in stadium:
    venue = df.query('venue == @i')
    print('At {} :'.format(i))
    
    #query to find the toss data alone
    toss_query = venue.query('toss_winner == winner')
    
    #storing the result data in a list
    result_column = list(venue['result'])
    
    run_count = result_column.count('runs')
    wickets_count = result_column.count('wickets')
    
    #printing the values
    print("The Toss winner has won", len(toss_query), "times")
    print("Batting first won ", run_count, " times")
    print("Bowling first won", wickets_count, "times", end='\n\n')



























































'''
complete_data = {}   

df = pd.read_csv('IPL Matches 2008-2020.csv')

venues = df["venue"]

stadium = {}
n = 0
for a in venues:
    query = []
    venue_querry = df.query('venue == @a')
    print(venue_querry)
    for i in venue_querry:
        query.append(i)
    stadium[a] = [query]
    print(query)
    print(stadium)
    n += 1
    if n == 3:
        break



#df_2 = DataFrame(stadium)
#
#for k in df_2:
#    print(k)

'''