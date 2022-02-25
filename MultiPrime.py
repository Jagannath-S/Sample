from operator import truediv


print('code starts')
print('program to print prime numbers from 0 to n range')

def start():
    n = int(input('enter the n value ->'))
    prime(n)

def prime(n):
    num = 1
    i = 0
    while i < n:
       num += 1
       if is_prime1(num):
           print(num)
           i += 1
        

def is_prime1(num):
    if factor(num) == 2:
        return True
    else:
        return False

def factor(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    return count

start()

print('code ends')