#faulty calculator
num1=int(input("Enter number first "))
num2=int(input("Enter number second "))
opera=input("Enter the operation to be performed: ")
if opera=='*':
    if num1==45 and num2==3:
        print("The product of the both terms is: 555")
    elif num1!=45 or num2!=3:
        print("The product of the both terms is: ",num1*num2)
elif opera=='+':
    if num1==56 and num2==9:
        print("The sum of both the terms is: 77")
    elif num1!=56 or num2!=9:
        print("The sum of both the terms is: ",num1+num2)
elif opera=='/':
    if num1==56 and num2==6:
        print("The division of both the terms is: 4")
    elif num1!=56 or num2!=6:
        print("The division of both the terms is: ",num1/num2)