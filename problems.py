# q1
def greet(name ='user'):
    return 'hello ' + name +'!'
print(greet("ram"))
print(greet())
# -----------------------------
def get_sum(nums):
    sum=0
    for i in nums:
        sum += i
    return sum
print(get_sum([98,97,88]))
#  or use *args to take multiple arguments
def sum_all(*args):
    print(*args)
    return sum(args)
print(sum_all(1,34,5,6,4,5))
# -------------------------------------------------------------
def print_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")
print_kwargs(name= "krishna", age = 16 ,school ="ssvm")
print_kwargs(role = "engineer",department = "it",salary =100000000000000000000)
