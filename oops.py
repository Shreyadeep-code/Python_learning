
# class Car :
#     colour = "white"
#     brand = "BMW"
# car1 =Car()
# print(car1.colour)
# print(car1.brand)
# class Student :
#    # name = "Shreyadeep" #if init is not given then it is automatically created
#     colllege_name = "xyz" #class attribute
#     #constructor.
#     def __init__(self, name,marks):
#         self.name = name #obj attribute(higher priority)
#         self.marks =marks
#     #methods
#     def hello(self): 
#         print("hello")
#     def get_marks(self):
#         return self.marks
       
    
# s1 = Student("babul",90)
# print(s1.name,s1.marks)
# s2 =Student("ajju",98)
# print(s2.name,s2.marks)
# print(s2.colllege_name)   
# s1.hello()
# print(s2.get_marks())
# class aspirant :
#     def __init__(self,name,marks):
#         self.name =name
#         self.marks=marks
#     def get_avg(self):
#         sum =0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your average is",sum/3)
#     @staticmethod #object is not required here
#     def comment():
#         print("nice result")
# #enter 3 marks of the aspirant
# s1 = aspirant("ram",[98,89,90])
# s1.get_avg()
# s2 = aspirant("shreyadeep",[99,98,96])
# s2.get_avg()
# del s1
#s1.get_avg()#this show error as s1 is deleted.
#s1.name ="raj"
#s1.get_avg()
#ABSTRACTION--> (showing essential things to user)
# class Account :
#     def __init__(self,balance,account_no,acc_pass):
#         self.balance =balance
#         self.account_no = account_no
#         self.__acc_pass = acc_pass#private things can only accessed inside the class.
#     def credit(self,amount):
#         self.balance +=amount
#         print(amount,"rs was credited")
#     def debit(self,amount):
#         if(amount<=self.balance):
    #         self.balance -=amount
    #         print(amount,"rs was debited")
#         else:
    #         print("insufficient balance!")
#     def check_balance(self):
#         return self.balance
# acc1 = Account(100000,12345,"abcde")
# #print(acc1.__acc_pass)#show error, give two'_'to make private

# acc1.credit(5000)

# acc1.debit(19000)
# print(acc1.check_balance()) 
# ----------------------------------------------------------------------------------------------------------------------- 
 #INHERITANCE -->
# class CAR :
#         def __init__(self,type):
#              self.type =type
             

#         @staticmethod
#         def start():
#             print("car started")
#         @staticmethod
#         def stop():
#             print("car stopped")
# class Toyotacar(CAR):
#     def __init__(self,name,type):
#         self.name =name
#         super().__init__(type)
        
# # car1 =Toyotacar("fortuner")
# # car2 =Toyotacar("preius") 
# #car1.start()   
# #above class is a eg of single inheritance .
# class Fortuner(Toyotacar):
#      def __init__(self, brand):
#           self.brand =brand
# car3 =Fortuner("diesel")
# car3.start()
# car4 = Toyotacar("prius","electric")
# print(car4.type)
# car4.start()
# # above is the example of multilevel inheritance
# #multiple inheritance.
# class A :
#     varA = "welcome to class a"
# class B :
#      varB = "welcome to class b"
# class C (A,B) :
#      varC = "welcome to class c"

# c1 = C()
# print(c1.varA)
# ---------------------------------------------------------------------------------
# class Person :
#     name = "anonymous"
#     # def change_name(self) :
#     #     self.name = name  #a new obejct is created,to access the name in class use Person.name or self.__class__.name
#     # or
#     @classmethod
#     def change_name(cls,name) :
#         cls.name =name


# p1 =Person()
# p1.change_name("raghu")
# print(p1.name)
# print(Person.name)
# ----------------------------------------------------------------------------------------------------------------------
# class student:
#     def __init__(self,phy,chem,math):
#         self.phy =phy
#         self.chem =chem
#         self.math =math
#         # self.percentage = str((self.phy +self.chem+self.math)/3) +"%"
#         #if you update any mark of the student then percentage will not update, so use @property method to update
#     @property
#     def percentage(self):
#         return str((self.phy +self.chem+self.math)/3) +"%"
# stu1 = student(98,97,90)
# print(stu1.percentage)  
# stu1.phy =95
# print(stu1.phy)     
# print(stu1.percentage)

# -----------------------------------------------------------------------------------------------------------
# class Complex :
#     def __init__(self,real,img):
#         self.real =real
#         self.img =img
#     def show_number(self):
#         print(self.real,"i +",self.img,"j")
#     def __add__(self,num2):
#         newreal = self.real +num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal,newimg) 
#     def __subtract__(self,num2):
#         newreal = self.real -num2.real
#         newimg = self.img - num2.img
#         return Complex(newreal,newimg) 
# num1 = Complex(1,3)
# num1.show_number()
# num2 = Complex(4,6)
# num3 =num1+num2
# num3.show_number()      
# -----------------------------------------------------------------------------------------------------------------
# class circle :
#     def __init__(self,r):
#         self.r =r
#     def Area(self):
#         print("area is :",3.14*self.r*self.r)
#     def Perimeter(self):
#         print("perimeter is :",2*self.r*3.14)
# c1 = circle(4)
# c1.Area()
# c1.Perimeter()
# --------------------------------------------------------------------
class Employee :
    def __init__(self,role,dept,sal):
        self.role =role
        self.dept = dept
        self.sal = sal
    def show_detail(self):
        print("role is :",self.role,"\n")
        print("department is :",self.dept,"\n")
        print("salary is :",self.sal)
e1 = Employee("accountant","commercial",10000000)
e1.show_detail()
class Engineer(Employee) :
    def __init__(self,name,age):
        self.name =name
        self.age =age
        super().__init__("Engineer","IT",7000000000)

engg1 = Engineer("Ram","20")
engg1.show_detail()
print(engg1.name)
# ------------------------------------------------------------------------------------------
class Order :
    def __init__(self,order,price):
        self.order = order
        self.price = price
    def good_order(self,ord2):
        return self.price <ord2.price
    
order1 =Order("tea",20)
order2 = Order("coffe",50)
print(order2.good_order(order1))

        
     
        
     


      
      
  
 
        
