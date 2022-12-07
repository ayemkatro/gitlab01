def is_year_leap(year):
    #
    # Your code from the previous LAB.
        if year%100:
            if year%4:
                return False
            else:
                return True
        else:
            if year%400:
                return False
            else:
                return True
        #
    #

def days_in_month(year, month):
    #
    # Write your new code here.
    year = is_year_leap(yr)
    if year:
        day=[31,29,31,30,31,30,31,31,30,31,30,31]
        xx=day[month-1]
        return xx

    else:
        day=[31,28,31,30,31,30,31,31,30,31,30,31]
        xx=day[month-1]
        return xx
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")