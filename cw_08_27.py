# Python review CW
# Problem 1:
# Create code and define the variable below outside of any function.
# After you create the list variable write a function called ```stupid_array_tricks```
# that takes an array as a parameter, and performs the functions listed below in the instructions.
# ```
# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# ```
# a) Print the 2nd and 3rd elements of the person_array using a *range*
# b) Print the last 2 elements of the person_array using a *range*
# c) Insert the new element ```Chuck``` between the 2nd (```Kevin```) and 3rd (```Erin```) elements
# d) Take out the 2nd element (```Kevin```) from the list
person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
print(person_array[1:3])
person_array.insert(2,"Chuck")
print(person_array)
indx=person_array.index("Kevin")
print(indx)
person_array.pop(1)
print(person_array)

# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q',
# ask them to input another string.
def quittingFunc():
    userinput=0
    while(userinput!='q'):
        userinput=input("Enter a String or q to quit: ")
quittingFunc()

# Problem 3:
# Create a function that uses the data list below.
# ```
# ['GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'DECENT_DATA',
# 'GOOD_DATA'
# 'BAD_DATA',
# 'GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'GOOD_DATA']
# ```
# Write the code to do the following:
# * Print the length of the original DATA list/array (ex. ```Starting length of data list is 10```)
# * Remove all ```BAD_DATA``` from the DATA list/array
# * Print the length of the final DATA list/array (ex. ```Ending length of data list is 7```)
data_list=['GOOD_DATA','DECENT_DATA','BAD_DATA','DECENT_DATA','GOOD_DATA','BAD_DATA','GOOD_DATA','DECENT_DATA','BAD_DATA','GOOD_DATA']
print(f'Starting length of data list  is {len(data_list)-1}') # !! : len() returns the lenght, no need to subtract 1
for x in data_list:
    if x == "BAD_DATA":
        index= data_list.index(x)
        data_list.pop(index)
        print(data_list) # !! : no need to print the list for each iteration 
print(f'Ending length of data list is {len(data_list)-1}') # !! : len() returns the lenght, no need to subtract 1

# Problem 4:
# Use the following list of 5 numbers.
# ```score_list = [21,14,6,8,28,42,21]```
# Write the code to do the following:
# * Print the sum of the numbers (ex. ```The SUM of the numbers is 140 ```)
# * Print the maximum value from the numbers (ex. ```The MAX of the numbers is 140 ```)
# * Print the minimum value from the numbers (ex. ```The MIN value of the numbers is 6 ```)
score_list = [21,14,6,8,28,42,21]
print(f'\nThe sum of the numbers is  {sum(score_list)}\n')  # * Print the sum of the numbers
print(f'The maximum of the numbers is  {max(score_list)}\n')# * Print the maximum value from the numbers
print(f'The minimum of the numbers is  {min(score_list)}\n')# * Print the minimum value from the numbers

# ### Challenge:
# Create a program that will let the User build a list words.
# Prompt the User for a word. Add the word the User enters and add it to the list.
# Allow the User to keep entering words until they enter 'x' to exit the program.
#
# Print the final word list prior to exiting the program.
def wordFunc():
    string_list =["peace","love","emphathy","share","care"]
    userString=""
    while(userString != 'q'):
        string_list.append(userString)
        userString=input("Enter a word here: ")
    return string_list
print(wordFunc())
