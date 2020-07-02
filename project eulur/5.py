'''
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
testnum = 20
testing = True
while testing:
    testnum += 20
    for i in range(2,21):
        if testnum % i == 0 and i == 20:
            testing = False
        if testnum % i != 0:
            break
    
print(testnum)
