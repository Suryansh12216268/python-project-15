def factorial(x):
    """this is a recurive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x -1))
num = 5
print("the factorial of",num, "is", factorial(num))

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms =15
#check if the number of terms is valid
if nterms <= 0:
    print("please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))


def mysum(*args):
    sum1=0
    for i in args:
        sum1=sum1+i
    return(sum1)
print(mysum(1,2,3,4,5,6,7)) #7 arguments
print(mysum(1,2)) #2 arguments
print(mysum(1,2,3)) #3 arguments

def largestNumber(*numbers):
    m=numbers[0]
    for num in numbers:
        if num > m:
            m = num
    print("largest:",m)
#write your code here
largestNumber(1,2,3,4)  #4 arguments
largestNumber(8,9,3,4,2,5)  #5 arguments

tax = lambda salary:salary*20/100
salary=int(input("please enter your salary:"))
print("Tax to be paid is", tax (salary))

doublenum = lambda x: x*2
a=int(input("a: "))
print(doublenum(a))
x = lambda a, b: a*b
print(x(5, 6))


def squares(x):
    return x**2
list1=[1,2,3,4,5]
#using the square function inside map functions
print(list(map(squares, list1)))
# using lambda func inside the map

print(list(map(lambda x: x**2,list1)))
#using list comprehension to get equivalent behaviour as map
print ([x**2 for x in list1])


#filter function
a = [1,2,3,5,7,9]
b = [2,3,6,7,9,8]
print(list(filter(lambda x : x in a,b)))
print([x for x in a if x in b])


def largestinthree(a,b,c):
    if a > b and a > c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

num1=int(input("please enter a value for num1:"))
num2=int(input("please enter a value for num2:"))
num3=int(input("please entyer a vakue for num3:"))
result=largestinthree(num1,num2,num3)
print("Largest of the values entered is",result)

def computeGCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0)and(y%i==0):
                gcd=i
    return gcd
a=int(input("x:"))
b=int(input("y:"))
print(computeGCD(a,b))