f=open("./day4/day4input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

ans = 0
for l in a:
    l = l.split(",")
    x1 = [int(i) for i in l[0].split("-")]
    x2 = [int(i) for i in l[1].split("-")]
    print(x1, x2)
    if (x1[0]<=x2[0] and x1[1]>=x2[0]) or (x2[0]<=x1[0] and x2[1]>=x1[0]):
        ans+=1
print(ans)