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

def num_list_modifier(input_string, num_type):
    # modify string depending on if we want list of winning or acquired numbers
    if num_type == "winning":
        number_string = input_string[:input_string.find("|") - 1]
    
    elif num_type == "acquired":
        number_string = input_string[input_string.find("|") + 2:]

    output_numbers = number_string.split(" ")
    output_numbers = [i for i in output_numbers if i]
    output = [int(i) for i in output_numbers]
    return output
    
total_score = 0

for line in f:
    current_score = 0
    wn_count = 0 # number of winning numbers in a card
    
    input_text = line[(line.find(":")) + 2:]

    winning_numbers = num_list_modifier(input_text, "winning")
    acquired_numbers = num_list_modifier(input_text, "acquired")

    for i in acquired_numbers:
        if i in winning_numbers and wn_count == 0:
            current_score += 1
            wn_count += 1
        
        elif i in winning_numbers and wn_count >= 1:
            current_score *= 2
            wn_count += 1
    
    total_score += current_score

print(total_score)