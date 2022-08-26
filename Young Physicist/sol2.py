n = int(input())
s = 0
for i in range(n):
    x,y,z = map(int,input().split())
    s += x+y+z

if s == 0:
    print("YES")
else:
    print("NO")