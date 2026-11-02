def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

dici={"+":addition,"-":subtraction,"/":div,"*":mul}



a=int(input("enter first element: "))
inp=input("choose the operation (+ , - , / , *): ")
b=int(input("enter second element: "))

print(dici[inp](a,b))