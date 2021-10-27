#######################################################
# This script is used to analyse the data from a file
# The data used is IPL Matches data set from 2008 to 2020
# The stadium wise basic statistics have been displayed
# Author: 
# Created at: 22-10-2021
# Last Modified at: 26-10-2021
####################################################################################

import pandas as pd

import constants as c

df = pd.read_csv(c.STADIUM_DATA) # What is df here. Provide better name

stadium = df['venue'] # No need of explanation for every line. Comment needed only for complex code or for the function. 
stadium = set(stadium) # Converting to set is fine. There are some function in pandas itself to remove duplicates. Use that.

for i in stadium: # Always give meaningful name to iterataion. Dont use 'i'. ex. for stadium in stadiums:
    venue = df.query('venue == @i')
    print('At {} :'.format(i)) # Use f string instead of format.
    
    toss_query = venue.query('toss_winner == winner')
    
    result_column = list(venue['result'])  # Better name. There is inbuilt function to convert data series to list. to_list function I think. Check that.
    
    run_count = result_column.count('runs') # Is that represents run count??? or first batting won count
    wickets_count = result_column.count('wickets') # Is that represents wickets count??? or second batting count.
    
    #printing the values --- Never add comments for every action. Comments needed only if necessary (Complex logic)
    print("The Toss winner has won", len(toss_query), "times") # use f string.
    print("Batting first won ", run_count, " times")
    print("Bowling first won", wickets_count, "times", end='\n\n')

# Never ever have Zombie code. (Remove the code if it is not used. Dont comment and keep it in the program file.)

# It is iterating over all the stadium and calculates the winning stats. Check group by function. You dont need to use for loop.
