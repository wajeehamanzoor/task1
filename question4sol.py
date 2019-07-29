import string
vowel=['a','e','i','o','u']
alphabets=string.ascii_lowercase

for s in alphabets:
    if s in vowel:
        print("{} is a vowel".format(s))
    else:
        print("{} is a consonant".format(s))
