name=input("Enter a string : ")
letters=0
digit = 0
for s in name:
    if s.isalpha() == True:
        letters+= 1
    elif s.isdigit == True:
        digit += 1
print("Letters: ",letters)
print("Digits: ",digit)
