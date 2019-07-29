class charactercount:
    mystr = ""
    def isstring(self,data):
        if(type(data) == str ):
            self.mystr=data
        else:
            print("Invalid Input")
    def charCount(self):
        return len(self.mystr)
 
dd = charactercount()
dd.isstring(data="hello world")
print(dd.charCount())
