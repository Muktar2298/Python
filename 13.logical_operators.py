'''
#logical and operator
n1 = 10
n2 = 20
n3 = 30

if n1 > n2 and n1 > n3:
    print(f"{n1} is the largest number")

elif n2 > n1 and n2 > n3:
    print(f"{n2} is the largest number")

else:
    print(f"{n3} is the largest number")

'''

#vowel & consonant
word = input("Enter a alphabet character :")

if word == "a" or word =="e" or word == "i" or  word == "o" or word == "u" :
    print("Vowel!")
else :
    print("Consonent!")