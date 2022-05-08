# list = [13, 14, 8, 6, 18]

list = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    list.append(ele)

print("The sum of divisors are:")
for i in list:
    sum = 0
    for x in range(1, i):
        if(i % x == 0):
            sum = sum + x
    print(i, sum)
