print('CALCULATOR')
print('For Additon , Enter 1\nFor Subtraction , Enter 2\nFor Multiplication , Enter 3 \nFor Division , Enter 4\nFor Reminder , Enter 5\n')
sign=int(input('Enter your choice :- \n'))
num1=int(input('Enter the First Number:- \n'))
num2=int(input('Enter the second Number:- \n'))
def addition(num1,num2):
    return (num1+num2)
def subtraction(num1,num2):
    return (num1-num2)
def Multiplication(num1,num2):
    return (num1*num2)
def Division(num1,num2):
    return (num1/num2)
def Reminder(num1,num2):
    return (num1%num2)
if sign==1:
    print('Answer:- '+addition(num1,num2))
elif sign==2:
    print('Answer:- '+subtraction(num1,num2))
elif sign==3:
    print('Answer:- '+Multiplication(num1,num2))
elif sign==4:
    print('Answer:- ',Division(num1,num2)) 
elif sign==5:
    print('Answer:- ',Reminder(num1,num2))
else:
    print('Unknown Variable')




