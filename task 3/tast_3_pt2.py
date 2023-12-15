with open("C:\\Users\\euanc\\OneDrive\\Advent Coding Challenge\\Advent Coding Challenge Answers\\Advent-Of-Code-2023-Answers\\task 3\\t3.txt") as file:
    # read the file text into a variable
    data = file.read()

    # create an array, each element is a line of the text
    lines = data.strip().split("\n")

# length of the array
n = len(lines)

# length of line of text, all the lines are equal length
m = len(lines[0])

gear_numbers = [[[] for _ in range(m)] for _ in range(n)]

# Iterates through each element in a line of text, returning true if the 
# character iterated over is a symbol
def is_symbol(row, col, num):
    if not (0 <= row < n and 0 <= col < m):
        return False
    
    if lines[row][col] == "*":
        gear_numbers[row][col].append(num)

    return lines[row][col] != "." and not lines[row][col].isdigit()

ans = 0

# Iterate through each line, adding valid numbers to the ans variable as you go
for row, line in enumerate(lines):
    
    start = 0

    col = 0

    while col < m:
        start = col
        num = ""
        while col < m and line[col].isdigit():
            num += line[col]
            col += 1

        if num == "":
            col += 1
            continue

        num = int(num)

        # number ended, look around
        is_symbol(row, start - 1, num) or is_symbol(row, col, num)


        for k in range(start - 1, col + 1):
            is_symbol(row - 1, k, num) or is_symbol(row + 1, k, num)

for i in range(n):
    for j in range(m):
        nums = gear_numbers[i][j]
        if lines[i][j] == "*" and len(nums) == 2:
            ans += nums[0] * nums[1]
print(ans)