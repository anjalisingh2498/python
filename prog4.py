class ope:
        def __init__(self):
                self.l1=[]
        def accept(self):
                n=int(input("Enter the number of element:- "))
                for i in range(0,n):
                        e=int(input("Enter the element:- "))
                        self.l1.append(e)
                print("List:- ", self.l1)

        def __add__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]+other.l1[i])
                print("After addition:- ", newlist)
        def __sub__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]-other.l1[i])
                print("After Subtraction:- ", newlist)
        def __mul__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]*other.l1[i])
                print("After Multiplication:- ", newlist)
        def __floordiv__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]//other.l1[i])
                print("After floorDivision:- ", newlist)
        def __truediv__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]/other.l1[i])
                print("After Division:- ", newlist)
        def __mod__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]%other.l1[i])
                print("After Remainder Modulo:- ", newlist)

        def __lt__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]<other.l1[i])
                print("After lesser than:- ", newlist)

        def __gr__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]>other.l1[i])
                print("After Greater than:-", newlist)
        def __eq__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]==other.l1[i])
                print("After Greater than:-", newlist)

        def __ge__(self,other):
                newlist=[]
                for i in range(0,len(self.li))
                        newlist.append(self.l1[i]>=other.l1[i])
                print("After Greater Equal:- ", newlist)
        def __le__(self,other):
                newlist=[]
                for i in range(0,len(self.li))
                        newlist.append(self.l1[i]<=other.l1[1])
                print("After lesser Equal:- ", newlist)
