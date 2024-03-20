'''i=1
n=2
while i<=10:
    print(n,"*",i,"=",n*1)'''
'''my_tuple = (1, 2, 3, 'four', 7.0)
# Accessing elements
#print(my_tuple[0])
#print(my_tuple[3])
# Slicing
#print(my_tuple[1:4])
# Tuple unpacking
#a, b, c, d, e = my_tuple
#print(a, b, c, d, e)
# Tuple length
#print(len(my_tuple))
# Concatenating tuples
new_tuple = my_tuple + ('six', 7)
print(new_tuple)'''
# Creating a list
#my_list = [1, 2, 3, 'four', 6.0,4.02]
# Accessing elements
#print(my_list[5])
#print(my_list[3])
# Slicing
#print(my_list[1:4])
# Modifying elements
#my_list[0] = 'sachin'
#my_list[3] = 'doraemon'
#my_list[5] = 'miss'
#print(my_list)
# List length
#print(len(my_list))
# Appending an element
#my_list.append('six')
#print(my_list)
# Removing an element
#my_list.remove(3)
#print(my_list)
# List concatenation
#new_list = my_list + [7, 8]
#print(new_list)
# Creating a set
#my_set = {1, 2, 3, 3, 'six', 10}
#print("Set:", my_set)
# Adding elements to a set
#my_set.add(9)
#print("Updated Set:", my_set)
# Removing an element
#my_set.remove(3)
#print("Set after removal:", my_set)
# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Union of sets
#union_set = set1.union(set2)
#print("Union Set:", union_set)
# Intersection of sets
#intersection_set = set1.intersection(set2)
#print("Intersection Set:", intersection_set)
# Difference of sets
#difference_set = set1.difference(set2)
#print("Difference Set:", difference_set)

# Checking if an element is in the set
#print(2 in my_set)
# Set length
#print("Set length:", len(my_set)
'''thisdict = {"apple":55,"banana":65}
print(type(thisdict))
print(thisdict.keys())'''
#student={"name":"sachin","class":10,"address":"noida"}
#print(type(student))
#print(len(student))
#print(student["name"])
#print(student.keys())
#print(student.values())
#student.update({"master":2})
#print(student)
#def my_function():
 #   print("sachin")
#my_function()
'''def adding():
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    c=a+b
    print(c)
adding()'''
'''def substraction():
    a = int(input("enter the value"))
    b = int(input("enter the value"))
    c = a - b
    print(c)
substraction()'''
'''def multiplication():
    a = int(input("enter the value"))
    b = int(input("enter the value"))
    c = a*b
    print(c)
multiplication()'''
'''def square():
    a = int(input("enter the value"))
    b = int(input("enter the value"))
    b=a*a
    print(b)
square()'''
'''def swap():
    a = int(input("enter the value"))
    b = int(input("enter the value"))
    c=2
    a=c
    b=a
    print(c)
swap()'''
'''def even_odd():
    a=int(input("enter the number"))
    if (a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
even_odd()'''
'''def prime_number():
    a=int(input("enter the value of prime"))
    for i in range(2,a//2+1):
        if(a+i==0):
            print(i,"is not a prime number")
            break
        else:
            print(i,"is not prime number")
prime_number()'''
'''def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if( num == sum ):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
armstrong()'''
'''def max_min():
    a = int(input("enter the number"))
    b=int(input("enter the number"))
    if (a > b):
        print("a is max")
    elif (b > a):
        print("b is max")
    else:
        print("both are equal")
max_min()'''
#arguments
'''def my_para(x):
    print("hello",x)
my_para("sachin")'''
'''def my_para(a,b):
    print("hello",a,b)
my_para("sachin","shah")'''
#def sum(a,b):
 #   return a+b
#print(sum(20,30))
'''a=input("enter yor fist name :")
b=input("enter yor last name :")
def my_function(a,b):
     print(a,b)
my_function(a,b)'''
'''def my_function(*args):
    print("sachin",args[2])
my_function("sachin","sofcon","delhi")'''
'''f=open("C:\\Users\\Sachin\\OneDrive\\Desktop\\file handling\\sachin.txt","w")
f.write("")
f=open("C:\\Users\\Sachin\\OneDrive\\Desktop\\file handling\\sachin.txt","r")
print(f.read())
f=open("C:\\Users\\Sachin\\OneDrive\\Desktop\\file handling\\sachin.txt","a")
f.write("san")
f.close()'''
'''import math
#print(math.pow(2,2))
#print(math.floor(15.166))
#print(math.sqrt(72))
#print(math.log(1))
print(math.factorial(5))'''






