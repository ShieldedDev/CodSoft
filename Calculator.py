num1 = int(input("Enter the 1st number: "))
num2 = int(input("\nEnter the 2nd number: "))
opr = input("\nEnter the operation (+,-,*,/): ")

if opr=='+':
    add=num1+num2
    print(num1,'+',num2,'=',add)

if opr=='-':
    subtract=num1-num2
    print(num1,'-',num2,'=',subtract)

if opr=='*':
    multiply=num1*num2
    print(num1,'*',num2,'=',multiply)

if opr=='/':
    divide=num1/num2
    print(num1,'/',num2,'=',divide)
