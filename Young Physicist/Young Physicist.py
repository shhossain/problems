# Young Physicist

n = int(input())

codordinates = []
for i in range(n):
    x,y,z = map(int,input().split())
    codordinates.append((x,y,z))

x = 0
y = 0
z = 0
for i in codordinates:
    x += i[0]
    y += i[1]
    z += i[2]

if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")