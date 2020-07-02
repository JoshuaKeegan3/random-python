#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

testnum = 1
primes=0
while primes < 10:
    if testnum %2 == 0:
        for i in range(2,int(testnum/2)):#check the testnum+1
            if testnum % i == 0:
                break
            if i == testnum/2-1:
                primes += 1
    else:
        for i in range(2,int(testnum/2 +0.5)):
            if testnum % i == 0:
                break
            if i == testnum/2-0.5:
                primes += 1
    testnum+=1

print(testnum)
