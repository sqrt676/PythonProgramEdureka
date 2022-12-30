def factorial(n):
    ans=1
    while n>=2:
        ans*=n
        n=n-1
    return ans
x=int(input())
print(factorial(x))