from math import factorial as fact

print('Code started')
print('Program to find if the number is strong num or not')


def start():
    num = int(input('Enter a number ->'))
    temp = num
    sum = strong(num)
    is_strong(temp, sum)

def strong(num):
    sum = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        sum = sum + fact(rem)
    return sum

def is_strong(temp,sum):
    if temp == sum:
        print(f'{temp} is a strong number')
    else:
        print(f'{temp} is not a strong number')

start()

print('code ends')