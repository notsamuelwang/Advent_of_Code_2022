f = open("in.txt")
a=[0]
for l in f.readlines():
    l = l.removesuffix('\n')
    if l=='':
        a.append(0)
    else:
        a[-1]+=int(l)
print(sum(sorted(a)[-3:]))