f=open("./day3/day3input.txt")
ans = 0
for l in f.readlines():
    l = l.removesuffix("\n")
    x = l[:len(l)//2]
    y = l[len(l)//2:]
    found = False
    for i in x:
        if i in y and not found:
            if i==i.lower():
                ans+=ord(i)-ord('a')+1
            else:
                ans+=ord(i)-ord('A')+27
            found = True
print(ans)