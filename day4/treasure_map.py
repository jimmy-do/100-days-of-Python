# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# Your job is to write a program that allows you to mark a square on the map using a two-digit system.

# The first digit in the input will specify the column (the position on the horizontal axis).

# The second digit in the input will specify the row number (the position on the vertical axis).

# Example Input 1

# column 2, row 3 would be entered as: 23

# Example Output 1

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']

# Example Input 2

# column 3, row 1 would be entered as: 31

# Example Output 2

# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')

position = input('Where do you want to put an X? ')

x = int(position[0])
y = int(position[1])

map[y-1][x-1] = 'X'

print(f'{row1}\n{row2}\n{row3}')
