list=[]
n=input("Enter a range for yor list: ")
n=int(n)
for s in range(0,n):
    x=input("Enter a number you want to have in list: ")
    x=int(x)
    list.append(x)
min=list[0]    
for s in list:
    if s < min:
        min=s
print(min)