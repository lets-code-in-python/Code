# Given a 2D array, print it in spiral form.

# 2d list is given
lst=[[x for x in range(y,y+4)]for y in range(0,5*4,4)]
print(lst)
'''[[0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18, 19]]'''

#required output is
'''0 1 2 3 
7 6 5 4 
8 9 10 11 
15 14 13 12 
16 17 18 19 '''

for i in range(len(lst)):
    if i%2==0:
        for j in lst[i]:
            print(j,end=" ")
        print()
    else:
        for j in range(-1,-len(lst[i])-1,-1):
            print(lst[i][j],end=" ")
        print()

