# basic while loop
""" i = 1
while i <= 100:
    print(i)
    i = i + 1

print("Loop is Completed") """


"""
 # sum of 10 numbers
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum) """


#sum of n numbrs
sum = 0
i = int(input("Enter the initialization number :"))
n = int(input("Enter the limit of number:"))

while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
