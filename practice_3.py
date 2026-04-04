"""a = int(input("enter a number"))
def square_func(a) :
    return(a**2)
print(square_func(a))"""

"""def sum(a,b) :
    return a+b
s = sum (3,4)
print("sum is",s)"""

def multiply(a,b) :
    return a*b 
print(multiply('a',2))
"""def circle(a) :
    area = a*3.14*a
    circumference = 2*3.14*a
    return area,circumference
a,c = circle(3)
print("AREA IS",a,"\nCIRCUMFERENCE IS",c)"""
"""def greet(name = "user") :
    return 'Hello' +' '+ name+'!'
print(greet())"""
cube = lambda a : a**3
print(cube(7))
arr = [2,4,7,8,9]
sum = 0
for i in range (len(arr)) :
    sum = sum + arr[i]
print(sum)