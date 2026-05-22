day = int(input())
month = int(input())
year = int(input())

# check valid year
if year <= 0:
    print("Invalid Date")

# check valid month
elif month < 1 or month > 12:
    print("Invalid Date")

else:
    # leap year check
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = True
    else:
        leap = False

    # days in month
    if month in [1,3,5,7,8,10,12]:
        max_day = 31
    elif month in [4,6,9,11]:
        max_day = 30
    elif month == 2:
        if leap:
            max_day = 29
        else:
            max_day = 28

    # validate day
    if day < 1 or day > max_day:
        print("Invalid Date")
    else:
        # increment date
        day += 1

        if day > max_day:
            day = 1
            month += 1

            if month > 12:
                month = 1
                year += 1

        print(f"{day:02d}-{month:02d}-{year}")
