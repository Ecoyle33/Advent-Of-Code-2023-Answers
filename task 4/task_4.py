# pseudo code:
# read the data into the program
# remove the key from the string and split the string into two variables
# first variable is a set containing the 'winning numbers'
# second variable contains all the 'numbers you have'
# create two more variables storing the current and total scores of the cards
# create a final variable keeping track of the number of winning numbers (wn_count) in the second variable
# iterate through the 'numbers you have', checking each time if they match one of the winning numbers
# if they match and wn_count == 0, add 1 to current score and add 1 to wn_count
# if they match and wn_count >= 1, double the current score and add 1 to wn_count
# once you've iterated through the numbers you have, add the final score from the current card to the total score
# repeat the previous steps for each card in the pile
# return the total score

f = open("C:\\Users\\euanc\\OneDrive\\Advent Coding Challenge\\Advent Coding Challenge Answers\\Advent-Of-Code-2023-Answers\\task 4\\t4.txt", "r")

for line in f:
    current_score = 0
    total_score = 0
    wn_count = 0 # number of winning numbers in a card
    
    input_text = line[(line.find(":")) + 2:]
