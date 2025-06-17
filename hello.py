'''print("Hello World")
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
print(dict1.values())'''

def add():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    sum = int(num1) + int(num2)
    print("The sum is:", sum)
add()