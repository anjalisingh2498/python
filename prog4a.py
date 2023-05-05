from lab4 import*

obj1=ope()
obj2=ope()

obj1.accept()
obj2.accept()

while True:
        print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.FloorDivision \n 5.Division \n 6.Remainder Modulo  \n 7. Lesser than \n 8. Greater than \n 9.Equal \n 10. Greater Equal \n 11. Lesser Equal \n 12. Exit")>
        ch=int(input("Enter the choice:- "))
        if ch==1:
                obj1+obj2
        elif ch==2:
                obj1-obj2
        elif ch==3:
                obj1*obj2
        elif ch==4:
                obj1//obj2
        elif ch==5:
                obj1/obj2
        elif ch==6:
                obj1%obj2
        elif ch==7:
                obj1<obj2
        elif ch==8:
                obj1>obj2
        elif ch==9:
                obj1==obj2
        elif ch==10:
                obj1>=obj2
        elif ch==11:
                obj1<=obj2

        else:
                break
