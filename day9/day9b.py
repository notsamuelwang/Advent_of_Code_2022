f=open("./day9/day9input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n").split(' '))

v = {}
x = [0]*10
y = [0]*10
for l in a:
    for i in range(int(l[1])):
        if l[0]=='R':
            x[0] += 1
        if l[0]=='L':
            x[0] -= 1 
        if l[0]=='U':
            y[0] += 1
        if l[0]=='D':
            y[0] -= 1
        for j in range(9):
            if abs(x[j]-x[j+1])>=2 or abs(y[j]-y[j+1])>=2:
                if y[j]!=y[j+1]:
                    if y[j]>y[j+1]:
                        y[j+1] += 1
                    else:
                        y[j+1] -= 1
                if x[j]!=x[j+1]:
                    if x[j]>x[j+1]:
                        x[j+1] += 1
                    else:
                        x[j+1] -= 1
        v[(x[9], y[9])]=1
print(len(v))