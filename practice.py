def fact_num (n) :
    fact =1
    i=1
    for i in range(1,n+1) :
        fact =fact *i
        i+=1
    print(fact)
n = int(input("enter the number"))
# fact_num(n)
student =["Shreyadeep Parida", 20, "Nuapada"]
def print_list(list) :
     for items in list :
         print(items, end = ",")
print_list(student)
print(student)
def check_num(a):
    if(a%2 == 0) :
        print("EVEN")
    else :
        print("ODD")
n = int(input("enter a number"))
# check_num(n)
def fact(n) :
    if(n == 0 or n == 1):
        return 1
    else :
        return n * fact(n-1)
# print(fact(3))
def sum_nums(n):
    if(n == 1) :
        return 1
    else :
        return n + sum_nums(n-1)
# print(sum_nums(4))