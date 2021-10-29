"""
1. if...else
2. if...elif...else
3.inner statement
4.ternary operator

"""
###############
''' 
1. if--else
# pass / fail 
string = input("Enter Student Obtained Markss:")
marks = int(string)

if marks >= 33 : 
    print("Your Passed.Congratulation!")
else :
    print("You failed.Try Again")


# even / odd 
numberInSting = input("Enter Student Obtained Markss:")
number = int(numberInSting)

if number % 2 == 0 :
    print(f"{number} : Is a Evne Number")
else :
    print(f"{number} : is Odd Number")    

'''

##############
'''
2.if..elif..else
#letter Grade 
inputInString = input("Enter Your Marks : ")
inputInNumber = int(inputInString)

if inputInNumber >= 80 :
    print("A+")
elif inputInNumber >= 70 :
    print("A")
elif inputInNumber >= 60 :
    print("A-")
elif inputInNumber >= 50 :
    print("B")
elif inputInNumber >= 34 :
    print("C")
else:
    print("You Failed in Exam") 

'''


###############
''' 
3.inner statement
#find the largest number
n1 = 10
n2 = 20
n3 = 30
#print(max(n1,n2,n3))
if n1 > n2 :
    if n1 > n3 : 
        print(f"{n1} is greater then {n2} & {n3} ")

if n2 > n1 :
    if n2 > n3 : 
        print(f"{n2} is greater then {n1} & {n3} ")

if n3 > n1 :
    if n3 > n2 : 
        print(f"{n3} is greater then {n1} & {n3} ")

'''



#################
'''
4.ternary operator
#find the largest number 

n1 = 30
n2 = 40

print(n1 if n1 > n2 else n2)

'''
