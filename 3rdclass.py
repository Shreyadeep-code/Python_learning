marks =[45, 78, 90, 0.7, 70]
#these changes can be allowed in list but not in strings 
#changes not allowed in tuples
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))
student =["Shreyadeep Parida", 20, "Nuapada"]
print(student)
print(len(student))
student[0] ="Shuprakash"
student[1] = 14
print(student)
print(marks[1:4])
num =[2,1,5,3,4,6]
num.append(7) #add the element at the end of the list
print(num)
"""num.sort() #sort the elements in ascending order
print(num)"""
num.reverse() #reverse the list
print(num)
num.sort(reverse =True) #sort elements indescendingorder
print(num)
num.insert(3,8) #insert the element at required position
print(num)
word =["ear","bat","cat","ant"]
print(word)
word.sort()
print(word)
word.sort(reverse =True)
print(word)
num.remove(5) #remove the firstoccurance of the element
print(num)
num.pop(4)#remove element at given index
print(num)
tup =('e','u','k','p','p')
print(tup)
print(tup[3])
tupl =(9,)#tuple having single element represented like this
#otherwise it taken as integer or character
print(tupl)
print(tup[1:3])
print(tup.index('k'))#position of the element in the tuple
print(tup.count('p'))#count the number of occurance