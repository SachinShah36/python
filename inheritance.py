'''class car:
    def dieselcar(self):
        a='mustang'
        b='bmw'
        print(a,b)
obj=car()
obj.dieselcar()

class car:
    def motorcar(self):
        c='audi'
        d='maruti'
        print(c,d)
obj=car()
obj.motorcar()'''
#class parent:
   # def my_fun(self,name):
      #  print("parent class is executed")
#obj=parent()
#print(obj.data)

'''class parent:
    def my_fun(self,name):
        self.name=name
        print(self.name)
obj=parent()
obj.my_fun("sachin")'''

'''class parent:
    def __init__(self,name,sale):
        self.name=name
        self.sale=sale
    def __str__(self):
        return f"{self.name}.{self.sale}"
    
obj=parent("sachin",2136111016)
print(obj)'''
'''class parent:
    def __init__(self):
        print("thid is non parameterized")
    def sofcon (self,name):
        print(name)
obj=parent()
obj.sofcon("sachin")'''
'''class parent:
    def __init__(self):
        print("tis is non parameter")
        def sofcon (self,name):
            print(name)
obj=parent
obj.sofcon("sofcon","delhi")'''
'''class parent:
    def __init__(self,name):
        print("this is non parameterized")
        def sofcon(self,name):
            print(name)
obj=parent
obj.sofcon("sachin")'''
'''
class parent:
    def first(self):
        print("parent class is executed")
class child:
    def child(sachin):
        print("this is a child class")
obj=child()  
obj=parent()  
obj.parent  '''  

'''class animal:
    def speak(self):
        print("sachin delhi")
class dog (animal):
    def bark(self):
        print("dog barking")   
d=dog()
d.bark()    
d.speak() '''   
'''class parent:
    def animal(self):
        print("animal")
class child(parent):
    def car(self):
        print("tiger")
class child1(child):
    def child(self):
        print("tiger")
class child2(child1):
    def child1(self):
        print("tiger")
obj=child()
obj.animal()
obj.car()
obj.child1()
obj.child2()'''
'''class parent:
    def car (self):
        print("car")
class child1(parent):
    def brand1(self):
        print("mustang")
class child2(child1):
    def brand2(self):
        print("bmw")
obj=child2()
obj.car()
obj.brand1()
obj.brand2()'''
''''class calculator:
        def sum(self,a,b):
                return a+b;
class calculation2:
        def multiply(self,a,b):
              return a*b;
class derived(calculator,calculation2):
        def divide(self,a,b):
               return a/b;
d=derived()
print(d.sum(12,6))
print(d.multiply(5,6))
print(d.divide(12,6))'''
'''class calculator:
        def sum(self,a,b):
               print(a+b)
class calculation2:
        def multiply(self,a,b):
               print(a*b)
class derived(calculator,calculation2):
        def divide(self,a,b):
               print(a/b)
obj=derived()
obj.sum(10,10)
obj.divide(12,3)
obj.multiply(4,2)'''
'''class calculator:
        a=int(input("value"))
        b=int(input("value2"))
        def sum(self,a,b):
               print(a+b)
class calculation2:
        def multiply(self,a,b):
               print(a*b)
class derived(calculator,calculation2):
        def divide(self,a,b):
               print(a/b)
obj=derived()
obj.sum()
obj.divide()
obj.multiply()'''
'''class parent:
    def vechicles (self):
        print("vechicles")
class child1(parent):
    def vechiles1(self):
        print("motor bike")
class child2(child1):
    def vechiles2(self):
        print(" diesel bike")
obj=child2()
obj.vechicles()
obj.vechiles1()
obj.vechiles2()'''
'''class animal:
    def speak(self):
        print("sofcon delhi")
class cs (animal):
    def bark(self):
        print("sofcon delhi")   
d=cs()
d.bark()    
d.speak()'''
'''class parent:
    def vechicles (self):
        print("vechicles")
class child1(parent):
    def vechiles1(self):
        print("motor bike")
class child2(child1):
    def vechicles2(self):
        print("bike")
class child3(child2): 
    def vechicles3(self):
        print("super bike")
class child4(child3):
    def vechicles4(self):
        print("Quad bike")
obj=child4()
obj.vechicles()
obj.vechiles1()
obj.vechicles2()
obj.vechicles3()
obj.vechicles4()'''
'''class animal:
    def speak(self):
        print("delhi")
class cs1 (animal):
    def bark(self):
        print("sofcon")  
class cs (cs1):
    def new(self):
        print(" delhi sofcon")  
d=cs()
d.bark()  
d.new()  
d.speak()'''
'''class india():
    def capital(self):
        print("new delhi is capital of india")
    def language(self):
        print("hindi language")
    def type(self):
        print("democratic country")   
class china():
    def capital(self):
        print("beijing")     
    def language(self):
        print("chinese")   
    def type(self):
        print("clever country")     
obj1=india()
obj1.capital()
obj1.language()
obj1.type()
obj=china()
obj.capital()
obj.language()
obj.type()'''
#class india():
 #   def capital(self):
    #    print("new delhi is capital of india")
   # def language(self):
  #      print("hindi language")
    #def type(self):
     #   print("democratic country")   
#class china():
 #   def capital(self):
  #      print("beijing")     
   # def language(self):
    #    print("chinese")   
    #def type(self):
#    print("clever country") 
#def func(obj):
 #   obj.capital()
  #  obj.language()
   # obj.type()
#obj_india=india()
#obj_china=china()
#func(obj_india)
#func(obj_china)


'''class india():
    def capital(self):
        return()
    def language(self):
        return()
    def type(self):
        return()   
class china():
    def capital(self):
        return()   
    def language(self):
        return()   
    def type(self):
        return()
    obj1=india()
    print(obj1.india ("new delhi is capital of india")) 
    print(obj1.india("hindi language")) 
    print(obj1.india("democratic country"))
    obj=china()
    print(obj.china ("beijing")) 
    print(obj.china("chinese")) 
    print(obj.china("clever country"))'''
'''def my_fuction():
    for i in range(0,10):
         print(i)
my_fuction()'''


# class Demo:

#     def fun_demo(self,temp=None):
#         if temp is None:
#             print("args is none")
#         else:
#             print("args is",temp)
            

# obj=Demo()
# obj.fun_demo()
# obj.fun_demo(10)

class Demo1:
      def fun_demo1(self):
            print("parents class fun executed")

class Demo2(Demo1):
      def fun_demo1(self):
            super().fun_demo1()
            print("child class fun executed")

obj=Demo2()
obj.fun_demo1()
