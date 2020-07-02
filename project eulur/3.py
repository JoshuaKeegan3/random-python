'''
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
'''
num=6000851475143
print('project 3')
for i in range (1, num // 2):
    if num==1:
        break
    if num % i == 0:
        for x in range(1, i+1):
            if i==x:
                num /= i
                print(i)
                break
