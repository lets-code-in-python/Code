# fib series is 0,1,1,2,3,5,8,....

#using loop

lst=[0,1]

n=int(input("enter the no for calculating fib at that position"))

for i in range(2,n):
    lst.append(lst[i-1]+lst[i-2])

print(n,"th position fib no is",lst[n-1])

print(lst)



