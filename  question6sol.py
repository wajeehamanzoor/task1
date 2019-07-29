list=[]
n=input("Enter a range for yor list: ")
n=int(n)
for s in range(0,n):
    x=input("Enter a number you want to have in list: ")
    x=int(x)
    list.append(x)
min1=list[0]
for s in list:
    if s <= min1:
        min1=s
list2=list.copy()        
list2.remove(min1)
min1=list2[0]
for s in list2:
    if s <= min1:
        min1=s
print(min1)        