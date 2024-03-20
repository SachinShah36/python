my_function()
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






