'''
#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
total_difference = 0
total1 = 0
total2 = 0
for i in range(1,101):
    total1 += i ** 2
    total2 += i
total2 **= 2
total_difference = total1-total2
print(total_difference ** 2)
