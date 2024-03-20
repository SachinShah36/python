a=int(input("enter the number"))
rev=0
temp=a
while(a>0):
 r=a%10
 rev=rev*10+r
 a//=10
if(temp==rev):
    print("pali")
else:
    print("not pali")