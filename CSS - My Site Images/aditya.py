def isCalculate(a,b):
    sum=a+b
    print("the sum is: ",sum)
    multi=a*b
    print("the product is: ",multi)
    if(a>b):
        print("first number is bigger")
    else:
        print("second number is bigger")

c=int(input("enter the number"))
d=int(input("input the no"))
isCalculate(c,d)
