import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height=test_h, width=test_w, cover=coverage):
    paint_cans = round(height * width / cover)
    if paint_cans >= 1:
        return paint_cans
    else:
        return 1


print(f'You will need {paint_calc()} can/cans.')

# print(round(14.6))
# print(math.ceil(14.6))
