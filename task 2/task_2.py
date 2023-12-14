n = 1 # number of games played through

# Sum of the game id's
id_sum = 0

# Sum of the product for max number of cubes
power_sum = 0

def max_value_checker(element, max_value):
    value = ''
    for char in element:
        if char.isdigit():
            value += char

    value = int(value)
    return max(value, max_value)

f = open('t2.txt', 'r')
for line in f:
    max_red = 0
    max_green = 0
    max_blue = 0
    
    # Adjust input text to remove game key, add 2 to remove space and colon itself
    input_text = line[(line.find(":")) + 2:]
    game_data = input_text.split(";")
    game_data = [i.split(", ") for i in game_data]

    sorted_data = []

    for i in game_data:
        sorted_data += i

    sorted_data = [s.strip() for s in sorted_data]

    for element in sorted_data:
        if element[(element.find(" ")) + 1:] == "red":
            max_red = max_value_checker(element, max_red)

        elif element[(element.find(" ")) + 1:] == "green":
            max_green = max_value_checker(element, max_green)
            
        elif element[(element.find(" ")) + 1:] == "blue":
            max_blue = max_value_checker(element, max_blue)
   
    power = max_red * max_green * max_blue

    if (max_red <= 12) and (max_green <= 13) and (max_blue <= 14):
        id_sum += n
        print(f"Valid game, id total: {id_sum}")

    else:
        print("Invalid game, too many cubes")
    
    n += 1
    power_sum += power

print(id_sum)
print(power_sum)