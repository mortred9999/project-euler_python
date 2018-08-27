'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

input  = 13
prime = []
prime_number = [2,]

for i in range(3,input):
    if (input % i ==0):
        pass
    else:
        prime_number.append(i)


print(prime_number)

'''
while (input % 2 ==0):
    prime.append(2)
    input = input //2

while(input % 3 == 0 ):
     prime.append(3)
     input = input //3

while(input % 5 == 0 ):
     prime.append(5)
     input = input //5

while(input % 7 == 0 ):
     prime.append(7)
     input = input //7

while(input % 11 == 0 ):
     prime.append(3)
     input = input //3


print(prime)'''