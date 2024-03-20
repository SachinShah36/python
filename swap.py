
'''b=int(input("value"))
# temp=a
#a=b
#b=temp
a=a+b
b=a-b
a=a-b1234
print(a)
print(b)'''
'''b=0
a=int(input("value"))

while a>0:
    digit = a % 10
    b= b* 10 + digit
    a //= 10
print(b)'''
'''a=int(input("enter the number"))
rev=0
temp=a
while(a>0):
 r=a%10
 rev=rev*10+r
 a//=10
if(temp==rev):
    print("pali")
else:
    print("not pali")'''


'''num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''
'''a=int(input("enter the value"))
for i in range(1, a+1):
    print(" ",end= " ")
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()'''
'''a=int(input("enter the value"))
for i in range(1, a+1):
    print(" ",end= " " )
    for j in range(a-i):
        print(" ",end="")
    for j in range(1, i+1):
        print("*", end=" ")
    print()'''
'''a=int(input("enter the num"))
for i in range (a):
    for j in range (a-i-1):
        print(" ",end="")
    for j in range (i+1):
        print("*",end=" ")
    print()
for i in range(a,-1,-1):
    for j in range (a-i-1):
        print(" ",end="")
    for j in range (i+1):
        print("*",end=" ")
    print()'''
'''a=int(input("enter the num"))
for i in range (a):
    for j in range (a-i-1):
        print(" ",end="")
    for j in range (i+1):
        print("*",end=" ")
    print()
for i in range(a):
    for j in range(i):
        print(" ", end="")
    for j in range(i, a):
        print("* ", end="")
    print()'''
'''a = [1, 2, 3, 'four', 6.0,4.02]
print(a[5])
print(a[3])
a.append("sachin")
a.insert(3,"mango")
a.remove(2)
a.__delitem__(4)
del(a[1])
a.sort()
print(a)'''
'''a = (1, 2, 3, 'four', 7.0)
b = a + ('six', 7)
a.insert(4,"sachin")
b.remove("six")

print(type(a))
print(a)'''
#disctionary
'''a={
    "name":"sachin", "age":"20"
   

}
#print(type(a))
#print(a.keys())
#print(a.values())
#for i in a:
#for i in 
for i in (a.keys()):
    for j in(a.values()):
        print(j)
    print(i)''' 


'''def my_function(firstname,lastname):
    print(firstname,lastname)
my_function("sachin","shah")'''

'''def my(x):
    return 5*x
print(my(5))'''

'''class my:
    x=10
    y=10
x1=my()
y2=my()
print(x1.x+y1.y)'''
'''class my:
    x=10
    y=5
x1= my()
y1= my()
print(x1.x+y1.y)
print(x1.x/y1.y)
print(x1.x-y1.y)
print(x1.x*y1.y)'''
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=a+b+c
if(a==60):
    print("equilateral triangle")
elif(b==60):
        print("equilateral triangle")
elif(c==60):
     print("equilateral triangle")
else:
        print("not equilateral triangle")
'''

'''a=int(input("enter"))
if(n =>'0'and n<='9'):
    print("digit")
elif(n>'a' and n<'z'):
    print("char")
'''
'''a=input("enter")
a=input("digit")
if(a>='0' and a<='9'):
    print("digit")
elif(a>='A' and a<='Z'):
    print("alfa")
else:
    print("special")'''
#a="hello"
#print(len(a))
'''a=10
class fact:
    b=20
    print(a,b)
    print(b)'''

'''
class fact():
        num=int(input("value"))  
        num=num**3
        print(num) '''


'''class fact():
    def get(self): 
        store=1
        num=int(input("Enter the number"))
        for i in range(1,num+1):
         store=store*i
        print(store)
obj=fact()
obj.get()'''
# class fact():
#     def get(self): 
#         store=1
#         num=int(input("Enter the number"))
#         for i in range(1,num+1):
#          store=store*i
#         print(store)
# obj=fact()
# obj.get()

'''class odd:
    def get(self):
        n = int(input('Enter a number'))
        if (n%2==0):
            print('The number is even')
        else:
            print('The number is odd')
            
obj=odd()
obj.get()'''
'''class prime:
    def check_prime(self,n):
        n=int(input("value"))
        cnt=0
        # nR1
        for i in range(1,int(n/2)+1):
            if(n % i == 0):
                cnt += 1
            else:
                i+=1
        if cnt > 0 :
            print(n,"is not a prime number")
        else:
            print(n,"is a prime number")

obj=prime()
print(obj.check_prime(6))'''
'''class calc:
    n=int(input("enter the value of n and m\n"))
    m=int(input("\nenter the value of m and n\n"))
    def add(self):
        x=calc.n + calc.m
        return x
    def subtract(self):
        y=calc.n - calc.m
        return y
    def multiply(self):
        z=calc.n * calc.m
        return z
    def divide(self):
        try:
            w=calc.n / calc.m
            return w
        except ZeroDivisionError as e:
            print("Error! Division by zero is not allowed.")

obj = calc()
print ("Addition:\t", obj.add())
print ("Subtraction:\t", obj.subtract())
print ("Multiplication:\t", obj.multiply())
try:
    print ("Division:\t", obj.divide())
except Exception as e:
    print("Error!\t",e) '''
'''class armstrong(object):
    num=int(input("Enter a three digit number \n"))
    sum=0
    temp=num
    digits=3
    while temp>0:
        digit=(temp%10)
        sum+=digit**digits
        temp//=10
        digits-=1
    if num==sum:
        print("%d is an Armstrong number" %num)
    else:
        print("%d is not an Armstrong number" %num) '''
'''class pali():
    s=""
def set_string(st):
    n=int(input("value"))
    global s
    s=st
    set_string(" ")
if s[::-1] == s:
    print("%s is a palindrome." %s)
else:
    print("%s is not a palindrome." %s)'''




 


    
        
        
   
      