# Leap years

# Check if a year is a leap year

def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test = [1992, 1600, 1900, 2002, 2020]

for num in test:
    print(f"{num} is a leap year: {leap_year(num)}")