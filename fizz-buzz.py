
def fizz_buzz(n):
    ans=[]

    for i in range(1,n+1):

        if i%3==0 and i%5==0 :
            ans.append("FizzBuzz")

        elif i%3==0 :
            ans.append("Fizz")

        elif i%5==0 :
            ans.append("Buzz")

        else:
            ans.append(str(i))

    return ans

# ans=fizz_buzz(15)
# print(ans)


def count_odd(low,high):

    return (high+1)//2 - (low//2)

print(count_odd(3,10))