"""numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
positve_num =0
for i in numbers :
    if(i>=0):
        positve_num +=1
print(positve_num)"""
"""even_sum =0
n = int(input("enter number"))
for i in range(0,n+1) :
    if(i % 2 == 0):
        even_sum +=i
print(even_sum)"""
"""n = int(input("enter number"))
for i in range(1,11) :
    print(n*i)"""
"""name = "SHREYADEEP PARIDA" 
reversed_name = ""
for char in name :
    reversed_name = char + reversed_name
print(reversed_name)"""
name = "SHREYADEEP PARIDA"
a = int(input("index of the character"))
for char in name :
    if(name.count(char) == a):
        print (char)
        break
n = int(input("enter number"))
while True :
    if(1<= n <= 10):
        print("thanks")
        break
    else :
        print("invalid")
        break




