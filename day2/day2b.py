f=open("day2input.txt")
ans = 0
for l in f.readlines():
    a = ord(l[0])-ord('A')
    b = ord(l[2])-ord('X')
    ans += 3*b + (a + b - 1)%3 + 1
print(ans)