"""f = open("demo.txt","r")
data = f.read()#if this one is executed then the cursor move to last of the file after this any readline command give empty space
print(data)#reading starts from where pointer is present
line1 =f.readline()#read one line at a time.
print(line1)
line2 =f.readline()
print(line2)
print(type(data))
f.close()"""
"""f = open("demo_txt","w")# after using w all the data of the file deleted and the new writings are added
f.write("I want to learn ml")
f.close()"""
"""f =open("demo_txt","a")# we can add data with existing data.
f.write("\nthen i learn dl")
#if a non existing file is append in w or a mode the it will be automatically created.
g = open("sample.txt","a")
g.write("hello guys")
g.close()"""
"""h= open("sample.txt","r+")#r+ mode can read from where pointer is present and over write from the begin and over write
h.write("hel")
h.close()
k = open("smple.txt","w")
k.write("maa jayguru")"""
#w+, a+ is also there.
#creates a new file to write in it.
#deletion operation
"""import os
os.remove('smple.txt')"""
"""f =open("practice.txt","w")
f.write("Hi everyone")
f.close()
f = open("practice.txt","a")
f.write("\nwe are learning file i/o")
f.write("\nusing java")
f.write("\ni like programming in java")"""
"""f = open("practice.txt","r")
data =f.read()
new_data =data.replace("java","python")
print(new_data)
f= open("practice.txt","w")
f.write(new_data)"""
def check_for_word():
    word = "learning"
    f = open("practice.txt","r")
    data = f.read()
    if(data.find(word) != -1) :
        print("found")
    else :
        print("not found")
#check_for_word()
def check_for_line() :
    word = "programming"
    with open("practice.txt","r") as f :
        data = True
        line_no =1
        while data :
            data = f.readline()
            if(word in data) :
                print(line_no)
                return
            line_no+=1
    return -1
check_for_line()
    

