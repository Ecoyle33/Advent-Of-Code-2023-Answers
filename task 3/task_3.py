with open("t3.txt") as file:
    # read the file text into a variable
    data = file.read()

    # create an array, each element is a line of the text
    lines = data.strip().split("\n")

# length of the array
n = len(lines)

# length of line of text, all the lines are equal length
m = len(lines[0])


def is_symbol(row, col):
    if not (0 <= row < n and 0 <= col < m):
        return False

    return lines[row][col] != "." and not lines[row][col].isdigit()

ans = 0

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
        if is_symbol(row, start - 1) or is_symbol(row, col):
            ans += num
            continue

        for k in range(start - 1, col + 1):
            if is_symbol(row - 1, k) or is_symbol(row + 1, k):
                ans += num
                break

print(ans)