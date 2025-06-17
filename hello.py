import random
print("Hello World")
name = "Aarush Kadam"
print(name)
print(name[0:6])
text = "Pyhton is a programming language."
t1 = text[0:7]
t2 = text[12:23]
t3 = t1+t2
print(t3)
multi_line_string = """
This is a multi-line string.
It can span several lines.
"""
print(multi_line_string)
n1 = "Aarush Kadam"
n2 = "Anand tripathi"
r1 = 7
r2 = 50
n3 = n1 + str(r1)
n4 = n2 + str(r2)
print(n3)
print(n4)
r3 = str(r1) + str(r2)
print(r3) 
name1 = input("Enter your name: ")
print(name1)
print(len(name1))
m1 = input("Enter your marks: ")
m2 = input("Enter teammate marks: ")
if(m1<m2):
    print("You have more marks than your teammate.")
elif(m1>m2):
    print("You have less marks than your teammate.")

rn = [10, 20, 30, 40, 50, 60]
rn.append(70)
rn.pop()
print(rn)
print(rn[2:5])
print(rn[::2])
rn.remove(30)
print(rn)
del rn[4]
print(rn)
test = [5, 5, 5, 5, 5]
test.remove(5)
print(test)
rn.sort(reverse=True)
print(rn)
print(rn.count(20))
dict1 = {"name": "Aarush", "age": 20}
print(dict1)
print(dict1.keys())
print(dict1.values())

def add():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    sum = int(num1) + int(num2)
    print("The sum is:", sum)
add()

for i in range(4):
    print(i)

for i in range(2, 10, 2):
    print(i)

while True:
    print("Your PC is hacked")

RandomNumber = random.randint(1, 10)
attempts = 3
while attempts > 0:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == RandomNumber:
        print("Congratulations! You've guessed the number.")
        break
    elif RandomNumber>guess:
        print("You have guessed the wrong number.")
        print("Random Number is greater than your guess.")
    elif RandomNumber<guess:
        print("You have guessed the wrong number.")
        print("Random Number is less than your guess.")
    attempts-=1
    print(f"You have {attempts} attempts left.")
if guess!=RandomNumber:
    print(f"Sorry, the correct number was {RandomNumber}.")

instrcutions = """1.Addition
2.Substraction
3.Multiplication
4.Division
5.Continue
6.Exit"""

def addition(a,b):
    print("Addition of two numbers is:")
    return a+b

def substraction(a,b):
    print("Difference of two numbers is:")
    return a-b

def multiplication(a,b):
    print("Multiplication of two numbers is:")
    return a*b

def division(a,b):
    print("Division of two numbers is:")
    return a/b

tocontinue = True
while tocontinue == True:
    print(instrcutions)
    inst=int(input("Enter your choice: "))
    a=int(input("Enter first number."))
    b=int(input("Enter second number."))
    
    if inst == 1:
        print(addition(a,b))
    elif inst == 2:
        print(substraction(a,b))
    elif inst == 3:
        print(multiplication(a,b))
    elif inst == 4:
        print(division(a,b))
    elif inst == 5:
        tocontinue = True
    elif inst == 6:
        tocontinue = False
    else:
        print("Invalid Choice.")