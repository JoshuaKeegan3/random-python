'''
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
'''
num = 0
numlist =[]
largestnum = 0
i=999
x=999
for i in range (999,100, -1):
    for x in range (999,100,-1 ):
        numlist.clear()
        num = i * x
        for number in str(num):
            numlist.append(number)
        if len(numlist)%2==0:
            for y in range(int(len(numlist)/2)):
                if numlist[0+y] != numlist[-1-y]:
                    numlist.append('false')
        else:
            for y in range(int(len(numlist)/2+0.5)):
                if numlist[0+y] != numlist[-1-y]:
                    numlist.append('false')
        if 'false' not in numlist:
            if i * x > largestnum:
                largestnum = i * x
print(largestnum)
