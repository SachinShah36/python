'''n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i+1):
       print("n",end="")  
       print("/n ")'''
a=int(input("inter your input :"))
for i in range(0,a):
  for j in range(0,a-i-1):
     print(end=" ")
  for j in range(0,i+1):
     print("*")
  print( )
revers primed
for i in range(a,0,-1):
    for j in range(0,a-i):
        print(" ")
        for j in range(0,i):
            print("*")
        print()


