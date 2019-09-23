#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
coder1 = 'hello world! python line " + 1
print(coder1)
# correced code by Xiao Min Chang
coder1 = 'hello world! python line' + '1'
print(coder1)
# new variable with an error for next member 
coder2 = when summer is gone + 2.0
print(coder2)
#correcred by Rebekah Reuben 
coder2 ='when summer is gone' + '2.0'
print(coder2)

# second group member's error to fix
coder3 = 'lions' + , + 'tigers' + , + 'and bears'
print(coder3)

#corrected by Laura Gravelsins 
coder3 = 'lions, ' + 'tigers, ' + 'and bears'
print(coder3)

#new variable with two errors for next member to fix  
coder4 = [seven, 8, 9, 9+'1']

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
#coder4

# etc. until all group members have fixed and made 1 error



#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt.index(-1)

# and then use missing_rt to remove the trial from rt
#multiple ways to do this -- unsure which one, but I think the second is more correct for this exercise
#this removes -1 from rt but creates a NoneType clean_rt list and doesn't need the index? 
clean_rt = rt.remove(-1)
#this removes -1 from rt based off index number an creates new list
clean_rt = rt[:4] + rt[5:]
#%%

#Laura Gravelsins: I think a simpler way is to use the delete function
#I think this part of the exercise requires us to use missing_rt in the code
clean_rt = del(rt[missing_rt])
print(clean_rt)

# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]


# try the same procedure. Does it work? 
# use a comment to explain why or why not below in comments

missing_rt_trouble = rt_trouble.index(-1)

#this doesn't work because index only returns the first index position, 
#and we would only know to remove that one whether we used the index method or the .remove method,
#since .remove only removes the first element, and index we would have to specify

#Laura Gravelsins: this doesn't work because rt_trouble.index(-1) only returns the position of the first missing rt (not the second), 
#so if we use the delete function: del(rt_trouble[missing_rt_trouble]), it will only remove the first missing rt, 
#because it is equivalent to del(rt_trouble[4])

# now write an if statement that you can use to remove the frist missing value 
# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.   

#the below code doesn't work -- fix later or someone else please fix :)

if -1 in rt_trouble:
    clean_rt = rt_trouble.remove(-1)
else: 
    clean_rt = rt_trouble
    
    
#%%

# for the last section, you will work with a list of lists:
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists

