
"""i =0
while i<5 :
    print(i)
    i+=1
print("new")
while i>=0 :
    print(i)
    i-=1"""
"""num = [1,4,9,16,25,36,49,64,81,100]
ind =0
while ind < len(num) :
    print(num[ind])
    ind +=1"""
"""i =1
while i < 8 :
    print(i)
    if(i == 3):
        
        break
    i+=1
i =0
while i<=5 :
    if(i ==3):
        i+=1
        continue #skip
    print(i)
    i+=1"""
#print even numbers
"""n = int(input("enter the number upto which you want to print the even numbers"))
i =0
while i<=n :
    if(i%2 != 0) :
        i+=1
        continue
    print(i)
    i+=1"""
#print odd numbers
"""n = int(input("enter the number upto which you want to print the odd numbers"))
i =0
while i<=n :
    if(i%2 == 0) :
        i+=1
        continue
    print(i)
    i+=1"""
# for loops
"""nums = [1,2,3,4,5]
fruits =["mango","apple","orange","banana"]
for val in nums:
    print(val)
for stock in fruits:
    print(stock)
name = "shreyadeep"
for char in name:
    if(char == 'y'):
          print("y found")
          break
    print(char)
else :
        print("end")"""

"""seq = range(5)# (stop)
print(range(5))
print(seq[0])
print(seq[1])
print(seq[3])
for el in seq :
    print(el)"""
for i in range(2,20,2) : # (start,stop,step)
    print(i)
for j in range(0,10,2) : # all even numbers
    pass
print("hi")