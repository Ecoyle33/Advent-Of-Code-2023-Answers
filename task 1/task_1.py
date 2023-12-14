"""--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, 
and you've been selected to take a look. The Elves have even given you a map;
on it, they've used stars to mark the top fifty locations that are likely to 
be having problems.

You've been doing this long enough to know that to restore snow operations, 
you need to check all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day 
in the Advent calendar; the second puzzle is unlocked when you complete the first. 
Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough")
and where they're even sending you ("the sky") and why your map looks mostly blank
("you sure ask a lot of questions") and hang on did you just say the sky 
("of course, where do you think snow comes from") when you realize that the Elves are already 
loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) 
has been amended by a very young Elf who was apparently just excited to show off her art skills. 
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a 
specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
Consider your entire calibration document. What is the sum of all of the calibration values?"""

# Function testing if a character in the string is a digit, used on line 59
def is_digit(x):
    
    if x.isdigit():
        return True
    else:
        return False

# Need to account for numbers represented by their names, i.e., 1 as 'one' and so on


def trebuchet():
    # Sum total that is returned at end of function
    total = 0

    # 'Collaboration document' - assume that means .txt file? If so, read text in from .txt file
    f = open("t1.txt", "r")

    number_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    p1 = 0
    p2 = 0
    # Separate each line into its own array
    for line in f:
        y = str(line.split('\n'))
        p1_digits = []
        p2_digits = []
        # Replace names of numbers with their corresponding digits
        for index, char in enumerate(y):
            if char.isdigit():
                p1_digits.append(char)
                p2_digits.append(char)

            for d, val in enumerate(number_names):
                if y[index:].startswith(val):
                    p2_digits.append(str(d + 1))

        p1 += int(p1_digits[0] + p1_digits[-1])
        p2 += int(p2_digits[0] + p2_digits[-1])

        
    print(p1)
    print(p2)

# lambda i: i.isdigit()
trebuchet()