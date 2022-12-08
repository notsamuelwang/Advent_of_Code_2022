f=open("./day8/day8input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

ans = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        w = 0
        if all([a[k][j]<a[i][j] for k in range(i)]):
            w = 1
        if all([a[k][j]<a[i][j] for k in range(i+1, len(a))]):
            w = 1
        if all([a[i][k]<a[i][j] for k in range(j)]):
            w = 1
        if all([a[i][k]<a[i][j] for k in range(j+1, len(a[0]))]):
            w = 1
        ans += w
print(ans)
    