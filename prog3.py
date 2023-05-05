d=dict()
class Employee:
        def input(self):
                self.name=input("Enter the name:- ")
                self.address=input("Enter the Address:- ")
                self.pan=input("Enter the Pan number:- ")
                self.basic_salary=int(input("Enter the basic salary:- "))
                self.cca=300
                self.hra=0.25*self.basic_salary
                self.da=0.4*self.basic_salary
                self.it=0.17*self.basic_salary
                self.gross_sal=self.basic_salary+self.hra+self.da+self.cca
                self.afterit=0.17*self.gross_sal
                self.net_sal=self.gross_sal-self.afterit
                self.update()
        def update(self):
                d.update({self.name:{
                        "Name":self.name,
                        "Address":self.address, 
                        "PAN Details":self.pan, 
                        "Basic Salary":self.basic_salary,
                        "CCA":self.cca,
                        "HRA":self.hra,
                        "DA" : self.da,
                        "IT":self.it,
                        "Gross salary" :self.gross_sal,
                        "Afterit":self.afterit,
                        "Net Salary":self.net_sal}})
        def search(self,name):
                flag=0
                for key in d:
                        if key == name:
                                print("Empolyee Found")
                                for i in d[key]:
                                        print(i, d[key][i])
                                        flag=1
                if flag==0:
                        print("Not Found")
        def display(self):
                for key in d:
                        print(key, d[key])



class employee1(Employee):
        emp=Employee()
        while True:
                ch=int(input("Enter the choice \n 1.Add 2.Print all Employees 3.Search 4.Exit \n"))
                if ch == 1:
                        emp.input()
                elif ch == 2:
                        emp.display()3
