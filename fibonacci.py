#this code is developed to print fibonacci numbers by sqrt676
def fib (n):
    if n==1:
        return ([0])
    elif n==2:
        return ([0,1])
    elif n>2:
        a=0
        b=1
        ans=[0,1]
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            ans.append(c)
        return ans
print(fib(int(input("enter number of terms in fib series"))))