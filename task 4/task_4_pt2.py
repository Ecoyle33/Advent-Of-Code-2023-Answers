def num_list_modifier(input_string, num_type):
    # modify string depending on if we want list of winning or acquired numbers
    if num_type == "winning":
        number_string = input_string[:input_string.find("|") - 1]
    
    elif num_type == "acquired":
        number_string = input_string[input_string.find("|") + 2:]

    output_numbers = number_string.split(" ")
    output_numbers = [i for i in output_numbers if i]
 
    return [int(i) for i in output_numbers]

with open("C:\\Users\\euanc\\OneDrive\\Advent Coding Challenge\\Advent Coding Challenge Answers\\Advent-Of-Code-2023-Answers\\task 4\\t4.txt") as file:
    data = file.read()

    lines = data.strip().split("\n")

winning_numbers = []
acquired_numbers = []

n = len(lines)
copies = [[] for i in range(n + 1)]

for card in lines:
    input_text = card[(card.find(":")) + 2:]

    w_num_list = num_list_modifier(input_text, "winning")
    acq_num_list = num_list_modifier(input_text, "acquired")

    winning_numbers.append(w_num_list)
    acquired_numbers.append(acq_num_list)

for i in range(n):
    winning_number_count = 0

    for num in acquired_numbers[i]:
        if num in winning_numbers[i]:
            winning_number_count += 1

    # use 'copies' to keep track of which lines need copying as we iterate through n
    for j in range(i + 1, i + winning_number_count + 1):
        copies[i].append(j)
score = [1 for i in range(n)]

# add number of copies to array of 1s, sum the element values to get the answer
for i in range(n-1, -1, -1):
    for j in copies[i]:
        score[i] += score[j]

print(sum(score))