alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']
inpt=input("enter if you want encode or decode:").lower()
def encode_decode(a,shift):
    b=''
    for i in range(len(a)):
        if a[i] in alphabet:
            d=alphabet.index(a[i])%26
            c=d+shift
            f=(alphabet[c])
            b+=f
        else:
            b+=" "
    print(b)
def something(inpt):
    a=input("enter any code:")
    shift=int(input("shift number: "))
    if inpt=="decode":
        shift*=-1
    encode_decode(a,shift)
something(inpt)