f=open("./day7/day7input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

class Node:
    def __init__(self):
        self.val = None
        self.s = 0
        self.data = {}
        self.up = None

root = Node()
root.val = "/"
cur = root
i = 0
while i<len(a):
    l = a[i].split(' ')
    if l[1] == 'cd':
        if l[2]=='/':
            cur = root
        elif l[2]=='..':
            cur = cur.up
        elif l[2] not in cur.data:
            newn = Node()
            newn.val = l[2]
            newn.up = cur
            cur.data[l[2]] = newn
            cur = cur.data[l[2]]
        else:
            cur = cur.data[l[2]]
    if l[1] == 'ls':
        i+=1
        while(i<len(a)):
            l = a[i].split(' ')
            if l[0]!='dir' and l[0]!='$':
                cur.s += int(l[0])
            elif l[0]=='$':
                i-=1
                break
            i+=1
    i+=1

nodes = []
q = [root]
while(q):
    x = q.pop()
    if x:
        nodes.append(x)
        for i in x.data:
            q.append(x.data[i])

ans = 0
for n in nodes:
    tot = 0
    q = [n]
    while(q):
        x = q.pop()
        if x:
            tot += x.s
            for i in x.data:
                q.append(x.data[i])
    if tot < 100000:
        ans += tot

print(ans)