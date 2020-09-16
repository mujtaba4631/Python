#Fibonacci Sequence -
#Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
n = int(input("enter the number till which you wanna generate Fibonacci series "))
a = 0
b = 1
c = a+1
print(a)
print(b)
for i in range(0,n):
    c = a+ b
    print(c)
    a,b=b,c
