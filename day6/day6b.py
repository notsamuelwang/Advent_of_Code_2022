f=open("./day6/day6input.txt")
a=[]
for l in f.readlines():
    a.append(l.removesuffix("\n"))

for l in a:
    s = l
    i=0
    while(len(set(s[i:i+14]))!=14):
        i+=1
print(i+14)