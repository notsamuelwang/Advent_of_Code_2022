f=open("./day5/day5input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

start = ["FTCLRPGQ", "NQHWRFSJ", "FBHWPMQ", "VSTDF", "QLDWVFZ", "ZCLS", "ZBMVDF", "TJB", "QNBGLSPH"]
stk = [[i for i in j] for j in start]

for l in a:
    l = l.split(" ")
    a = int(l[1])
    b = int(l[3])
    c = int(l[5])
    for i in range(a):
        stk[c-1].append(stk[b-1].pop())
print(''.join([i[-1] for i in stk]))