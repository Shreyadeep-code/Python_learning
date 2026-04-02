def func(a=5,b=6) :
   print(a*b)
   return a*b
    #return m
n1 = int(input("enter 1st number\n"))
n2 = int(input("enter 2nd number\n"))
#product = func(n1,n2)
#print("product is",product)
func()
def calc_avg(a,b,c) :
   
   avg = (a+b+c)/3
   print(avg)
   return avg
calc_avg(1,2,4)
# default values can be given to the variables used in function .
# if no argument passed during calling then default values are activated .
# Recurrsion
def show(n) :
   if(n==0) : # base case
      return 0
   print(n)
   show(n-1)
show(5)
