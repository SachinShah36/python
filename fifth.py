'''a=int(input("enter the number"))
#b=int(input("enter the number"))
if(a>b):
    print("a is max")
elif(b>a):
    print("b is max")
else:
    print("both are equal")
#a=int(input("enter the number"))
#b=int(input("enter the number"))
if(a>0):
    print("a is +")
elif(a<0):
        print("b is -")
else:
     print("0")'''
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if(a>b and a>c):
    print("a is max")
elif(b>a and b>c):
     print("b is max")
else:
     print("c is max")'''

'''if(a%2==0):
          print("even number")
else:
    
    print("odd number")'''
'''a=int(input("enter the number"))
b=int(input("enter the number"))
if(a>0 and b>0):
    print("quardinate 1")
elif(a<0 and b<0):
        print("quardinate 2")
elif(a>0 and b<0):
            print ("quardinate 3")
elif(a<0 and b>0):
                print("quardinate 4")'''

'''a=(input("enter the number"))

if(a.isalpha()):
    print("alpha")
elif(a.isdigit()):
    print("digit")
else:
    print("sep=")'''
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if(a+b+c==180):
    print("this is triangle")
else:
        print("not triangle")'''
        
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
if(a+b+c+d==360):
    print("this is a rectangle")
else:
        print("not rectangle")'''
'''alphabet=input("enter the alphabet")
vowel=['a','i','o','u','e','A','I','O','U','E']
if(alphabet in vowel):
         print(alphabet,'is a vowel')
else:
         print(alphabet,'is consonent')'''
'''a=int(input("enter the number"))
if(a==366):
    print("leap year")
else:
        print("not leap year")'''
'''a= int(input("Enter the first number "))
b= int(input("Enter the second number "))
c = int(input("Enter the third number "))
if(a>=b):
    print("return a")
elif(b>=c):
    print("return b")
else:
   iu print("return c")'''
'''sidea = int(input("Enter the length of the first side "))
sideb = int(input("Enter the length of the second side "))
sidec = int(input("Enter the length of the third side "))
if(a==b):
    print("return equilateral triangle")
elif(b==c):
        print("return equilateral triangle")
elif(a==c):
        print("return equilateral triangle")
else:
        print("return equilateral triangle")'''
'''a=int(input("enter your age"))
if(a>=18):
      print("you are eligible")
else:
      print("you are not eligible")'''
'''age=int(input("enter the age"))
salary=int(input("enter tha salary"))
if(age>=20):
    if(salary>=3000):
        print("increament")
if(age<=20):
    if(salary<=3000):
        print("not increment")'''
'''a=int(input("enter the number"))
if(a<100):
    if(a>80):
        print("a grade")
if(a<70):
    if(a>50):
        print("b grade")'''
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
for i in range(a,b,c):
    print(i)'''
'''a=int(input("enter the number"))
for i in range(1,10+1):
    print(i*a)'''
'''a=int(input("enter the number"))
fact=1
for i in range (1,a+1):
    fact=fact*i
    print(fact)'''
'''a=int(input("enter the number"))
for i in range(a,0,-1):
    print(i)'''
'''a=int(input("enter the number"))
for i in range(1,a+1):
    if(i%2==0):
        print(i)'''
'''a=int(input("enter the number"))
fact=0
for i in range(1,a+1):
    fact=fact+i
print(fact)'''
'''a=int(input("enter the number"))
i=0
while(i<100):
    print(i)'''
'''i=int(input("enter the number"))
while(i>=0):
    print(i)
    i-=1'''
'''a=int(input("enter the number"))
rev=0
while(a>0):
    r=a%10
    rev=rev*10+r
    a//=10
print(rev)'''
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
'''a=int(input("enter the number"))
sum = 0
temp=a
while(a>0):
     r= temp % 10
    sum=sum+(r*r*r)
  temp//= 10
if(temp==sum):
    print(num,"is an Armstrong number")
 else:
    print(num,"is not an Armstrong number")'''
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
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=a
a=b
b=c
print(a,b)'''
'''n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i+1):
        print("n",end="")
    print("\n")'''
'''n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i+1):
        print(j,end="")
    print(" ")'''
'''n=int(input("enter the number"))
for i in range(0,n+1):
    for j in range(i,n+1):
        print(j,end="")
    print(" ")'''
'''n=int(input("enter the num"))
val=65
for i in range(n):
    for j in range(i+1):
        alphabet=chr(val)
        print(alphabet,end="")
        val+=1
    print("\n")'''
'''n=int(input("enter the num"))
val=94
for i in range(0,n+1):
    for j in range(i,n+1):
        alphabet=chr(val)
        print(alphabet,end="")
        val+=1
    print("\n")'''
'''import datetime
x=datetime.datetime.now()
print(x.strftime("%m/%d/%y/%A/%H/%Y/%f/%S/%Z/%U/%j/%z/%B"))'''
'''a=["hello","sachin","doraemon","cartoon"]
print(a)
print(len(a))
print(type(a))'''
#a=["hello","sachin","doraemon","cartoon"]
#print(a)
#print(a[1])
#print(a[3])
#print(a[2:])
#print(a[:2])
#a.append("miss")
#print(a)
#a.insert(3,"think")
#print(a)
#a.remove("cartoon")
#print(a)
#a.pop()
#print(a)
#del a[3]
#print (a)
#a.sort()
#print (a)
#a=[9,5,3,6,7]
#a.sort(reverse=True)
#print(a)'
#b=[2,3,5,6,8]
#print(a+b)
'''import datetime
x=datetime.datetime.now()
print(x.strftime("%f"))'''
str = "aaaaa"
re = str[::-1]
pal = str
if (pal == re):
  print("string is palindrome ")
else:
  print("string is not pallindrome")


























        



         


        
    



    

