####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# print(s[0])
# print(s[3])
# print(s[2:5])
# print(s[1:4])
# print(s[4])



# Use indexing to print out the following:
# 'f'

# 's'

# 'ask'

# 'las'

# 'k'

# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
# mylist = [3,7,[1,4,'hello']]
# # Reassign "hello" to be "goodbye"

# mylist[2][2]= 'goodbye'

# print(mylist)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

set(mylist)
###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
