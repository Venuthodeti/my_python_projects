#this is not the actual code this is my imaginary code
inpt=input("enter if you want encode or decode:").lower()
if inpt=="encode":
    a=input("enter any code:")
    b=''
    shift=int(input("shift number: "))
    for i in range(len(a)):
        if a[i]!=" ":
            d=ord(a[i])+shift
            x=chr(d)
            b+=x
        else:
            b+=" "
    print(b)
elif inpt=="decode":
    a=input("enter any code:")
    b=''
    shift=int(input("shift number: "))
    for i in range(len(a)):
        if a[i]!=" ":
            d=ord(a[i])-shift
            x=chr(d)
            b+=x
        else:
            b+=" "
    print(b)
#this is not the actual code this is my imaginary code





