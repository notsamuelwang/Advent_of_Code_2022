f=open("./day8/day8input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

ans = 0
for i in range(1, len(a)-1):
    for j in range(1, len(a[0])-1):
        w = 1
        k = i-1
        while(k>=1 and a[k][j]<a[i][j]):
            k-=1
        w *= i-k
        k = i+1
        while(k<len(a)-1 and a[k][j]<a[i][j]):
            k+=1
        w *= k-i
        k = j-1
        while(k>=1 and a[i][k]<a[i][j]):
            k-=1
        w *= j-k
        k = j+1
        while(k<len(a[0])-1 and a[i][k]<a[i][j]):
            k+=1
        w *= k-j
        ans = max(w, ans)
print(ans)
    