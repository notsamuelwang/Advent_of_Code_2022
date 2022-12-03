f=open("./day2/day2input.txt")
ans = 0
for l in f.readlines():
    a = ord(l[0])-ord('A')
    b = ord(l[2])-ord('X')
    ans += 3*((b - a + 1)%3) + b + 1
print(ans)