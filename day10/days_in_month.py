year = int(input("Enter a year: "))
month = int(input("Enter a month: "))


def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print("Leap year.")
                return month_days[m-1]
            else:
                print("Not leap year.")
                return month_days[m-1]
        else:
            print("Leap year.")
            return month_days[m-1]
    else:
        print("Not leap year.")
        return month_days[m-1]


print(days_in_month(year, month))
