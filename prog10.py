import time
def caltime(func):
        def inner(*args):
                start_time=time.time()
                print("start time:- ",start_time)
                func()

                end_time=time.time()
                print("End time:- ",end_time)

                d=start_time-end_time
                print("Total time:- ", d)
        return inner

def Fibs():
        a,b=0,1
        while(1):
                yeild a
                a,b=b,a+b

n=int(input("Enter the value:- "))
@caltime

def my():
        fib=Fibs()
        for f in range(n-1)
                print(next(fib))
if "__main__":
        my()
