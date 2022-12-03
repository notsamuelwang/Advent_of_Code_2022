f=open("day3input.txt")
ans = 0
for l in f.readlines():
    ans = 0
    x = l[:len(l)/2]
    y = l[:len(l)/2]
    for i in x:
        if i in y:
            if i==i.lower():
                ans+=ord(i)-ord('a')+1
            else:
                ans+=ord(i)-ord('A')+27
print(ans)