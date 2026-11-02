def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b


yes=True
while(yes):
    a=int(input("enter first element: "))
    b=int(input("enter second element: "))
    inp=input("choose the operation (+ , - , / , *): ")
    if inp=="+":
        print(addition(a,b))
    if inp=="-":
        print(subtraction(a,b))
    if inp=="/":
        print(div(a,b))
    if inp=="*":
        print(mul(a,b))
    con=input("do you want to continue(y/n) :").lower()
    if con=="n":
        yes=False
        