f1=open("one.txt",'r')
f2=open("two.txt",'w')
for line in f1:
	f2.write(line)
f1.close()
f2.close()

while(1):
	print("Menu")
	print("1.Value Error \n 2. File Not Found Error \n 3.Type Error \n 4.IO Error \n 5.Name Error \n 0.Exit")
	ch=int(input("Enter the choice"))
	if(ch==1):
		try:
			f=open("one.txt",'z')
			print("Successful")
		except ValueError:
			print("Value Error")
	elif(ch==2):
		try:
			f=open("f5.txt",'r')
			print("Successful")
		except FileNotFoundError:
			print("File NOT Found")
	elif(ch==3):
		try:
			f=open("one.txt",'w','r')
			print("Successful")
		except TypeError:
			print("Type Error")
	elif(ch==4):
		try:
			f=open("one.txt",'w+')
			f2=open("f2.txt",'r')
			f2.write("newline")
		except IOError:
			print("IO Error")
	elif(ch==5):
		try:
			f=opens("one.txt",'r')
			print("Successful")
		except NameError:
			print("Name Error")
	else:
		break
