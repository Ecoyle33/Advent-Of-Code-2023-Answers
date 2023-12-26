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

with open("C:\\Users\\euanc\\OneDrive\\Advent Coding Challenge\\Advent Coding Challenge Answers\\Advent-Of-Code-2023-Answers\\task 4\\t4.txt") as file:
    data = file.read()

    lines = data.strip().split("\n")

winning_numbers = []
acquired_numbers = []

for card in lines:
    input_text = card[(card.find(":")) + 2:]

    w_num_list = num_list_modifier(input_text, "winning")
    acq_num_list = num_list_modifier(input_text, "acquired")

    winning_numbers.append(w_num_list)
    acq_num_list.append(acq_num_list)
