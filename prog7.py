class employee:
        raisee=1.5
        def __init__(self,first,last,empid,pay):
                self.first=first
                self.last=last
                self.empid=empid
                self.pay=pay

        def apply_raise(self):
                self.pay=self.pay*self.raisee
                print("after raise of employee pay = ",self.pay)

        def display(self):
                print("\nfirst name = ",self.first,
                        "\nlast name = ",self.last,
                        "\nemployee id = ",self.empid,
                        "\nemployee pay = ",self.pay)


class developer(employee):
        raiseee=1.7
        def apply_raise(self):
                self.pay=self.pay*self.raiseee
                print("\nafter raise of develper pay = ",self.pay)


class manager(employee):
        raiseee=1.8
        def apply_raise(self):
                self.pay=self.pay*self.raiseee
                print("\nafter raise of manager pay = ",self.pay)

obj1=employee("abc","he",1,50000)
obj2=developer("cde","ar",2,600000)
obj3=manager("pqr","si",3,70000)

obj1.display()
obj1.apply_raise()

obj2.display()
obj2.apply_raise()

obj3.display()
obj3.apply_raise()
