#1
print("print 11 to 100 using while loop:")

print("11 to 100 are printed below:")
i=11
while i<=100:
	print(i,i+1,i+2,i+3,i+4)
	i=i+5

#2
print("Calculate the sum from 1 to a given number:")
print("Input the last number")
n=int(input())
print("Sum from 1 to",n,"=",n*(n+1)/2)


#3
print("Find the fictorial of a given number")
print("Input the  number")
n=int(input())
x=1
k=n
while n:
	x=x*n
	n=n-1
print("Fictorial of",k, "=", x)



#4
print("printing all even number in a range:")
print("Input the intial number")
a=int(input())
print("Input the ending number")
b=int(input())
if a%2!=0:
	a=a+1
while a<=b:
	print(a)
	a=a+2


#5
print("Printing the multiplication table of a given number:")
print("Input the  number")
x=int(input())
for k in range(1,11):
	print(x,"×",k,"=",x*k)

#6
print("A simple calculator using function:")
print("Input 2 number")
p,q=map(int,input().split())
def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def mul(a,b):
   return a*b
def div(a,b):
   return a/b
w=add(p,q)
x=sub(p,q)
y=mul(p,q)
z=div(p,q)

print("sum =",w,"\n Difference=",x,"\nMultiplication =",y,"\n Division=",z)
