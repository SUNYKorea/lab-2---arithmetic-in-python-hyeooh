# TODO: Complete this function for task 1
# Use try-except block to handle errors
def check_number1(s):

    try:
        if(len(s)>2):
            s = int(s)
            s%= 100
            s = "0" + str(s)
    except ValueError:
        print("00")
    return s

# TODO: Complete this function for task 2
# Use string methods to handle errors
def check_number2(s):
    if s.isnumeric():
        if(len(s)>2):
            s = int(s)
            s%= 100
            s = "0" + str(s)
        return s
    else:
        print("00")

def go():
    year = input("Year of birth (YYYY): ")
    month = input("Month of birth (MM): ")
    day = input("Day of birth (DD): ")

    y1 = check_number1(year)
    m1 = check_number1(month)
    d1 = check_number1(day)

    print(y1 + m1 + d1) # Should print 020501 for 2002 May 1st

    y2 = check_number2(year)
    m2 = check_number2(month)
    d2 = check_number2(day)

    print(y2 + m2 + d2) # Should print 020501 for 2002 May 1st

go()

