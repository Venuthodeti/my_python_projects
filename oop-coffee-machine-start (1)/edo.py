inp=int(input())
ans=inp
rev=0
while inp>0:

    rev=rev*10+inp%10
    inp=inp//10
if rev==ans:
    print("YES")
else:
    print("NO")
print(rev)