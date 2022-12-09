f=open("./day9/day9input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n").split(' '))

v = {}
hx = hy = 0
tx = ty = 0
for l in a:
    for i in range(int(l[1])):
        if l[0]=='R':
            hx += 1
        if l[0]=='L':
            hx -= 1 
        if l[0]=='U':
            hy += 1
        if l[0]=='D':
            hy -= 1
        if abs(hx-tx)>=2 or abs(hy-ty)>=2:
            if hy!=ty:
                if hy>ty:
                    ty += 1
                else:
                    ty -= 1
            if hx!=tx:
                if hx>tx:
                    tx += 1
                else:
                    tx -= 1
        v[(tx, ty)]=1
print(len(v))