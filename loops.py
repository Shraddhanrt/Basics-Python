count = 1
while (count <= 5):
    print('Hello World')
    count += 1

i = 1
while i <= 5:
    print(i)
    i += 1

print("Loop Ended")

# print numbers from 1 to 100
a = 1
while a <= 100:
    print(a)
    a += 1

# print numbers from 100 to 1
b = 100
while b >= 1:
    print(b)
    b -= 1


# print multiplication table of number n
n = 5
i = 1
while i <= 10:
    print(n, 'x', i, '=', n*i)
    i += 1

# print the elements of the following list using a loop:
num=[1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(num):
    print(num[index]) #num[0], num[1]
    index += 1

# search for a number x in this tuple using loop:
num = (1,4,9,16,25,36,49,64,81,100)
x = 36
i= 0
while i < len(num):
    if (num[i] == x):
        print(x, 'is found at index', i)
        break
    i += 1
