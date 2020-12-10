# fib series is 0,1,1,2,3,5,8,....

#using recursion
def fib(x):
    if x==0 or x==1:
        return x
    return fib(x-1)+fib(x-2)
n=3
print(n,"th fib no is",fib(n-1))# we are taking first place  as 0 so for fib(n-1),we are  calculating for n-1

#using loop


