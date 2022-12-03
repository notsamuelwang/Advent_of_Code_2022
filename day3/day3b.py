f=open("./day3/day3input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

ans = 0
for i in range(len(a)//3):
    x = a[3*i]
    y = a[3*i+1]
    z = a[3*i+2]
    found = False
    for i in x:
        if i in y and i in z and not found:
            if i==i.lower():
                ans+=ord(i)-ord('a')+1
            else:
                ans+=ord(i)-ord('A')+27
            found = True
print(ans)