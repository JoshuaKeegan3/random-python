#This is not finished and doesn't quite work


def leaps(year1, year2 = 0):
    '''Takes two intergers as years in the revised Julian Calendar
returns the number of leap years inbetween them
Leap years are evenly divisable by four but not by 100
Except on years which the remainder when divided by 900 is 200 or 600
'''
    # defines a variable called leap_years
    leap_years = 0
    # Finds the smallest number
    if year1 > year2:
        temp = year1
        year1 = year2
        year2 = temp

    # small num to big num in jumps of four
    for i in range(year1, year2, 4):
        '''PROBLEM'''
        

        # if divisable by 100
        if i % 100 == 0:
            # if divided by 900 remainder not 200 or 600
            if i % 900 != 200 and i % 900 != 600:
                # add one
                leap_years += 1
        # else
        else:
            leap_years +=1
            # add one
        
    

    # Returns leap_years
    return leap_years
    


if __name__ == '__main__':
    l = leaps(0, 2000)
    print(l)

