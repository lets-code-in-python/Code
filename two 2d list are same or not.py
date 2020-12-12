
lst1=[[1,2,3],[4,5,6]]
lst2=[[1,2,3],[4,5,6]]
lst3=[[11,2,3],[4,5,6]]

# if two list are same then return yes else retuen No
f=0
for i in range(len(lst1)):
    for j in range(len(lst1[i])):
        if lst1[i][j]!=lst3[i][j]:
            print("No")
            f=1
            break
    if f==1:
        break
if f==0:
    print("yes")


