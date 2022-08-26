# beautiful_matrix

# input: a 5x5 matrix
matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))


# destinatiob point 3,3 - but beacause list start from 0, the point is 2,2
dp = [2, 2]

# find the locacaion of 1
p1 = [0, 0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            p1 = [i, j]
            break
    else:
        continue
    break
# distance between p1 and dp formyla d = abs(x1 - x2) + abs(y1 - y2)
d = abs(p1[0] - dp[0]) + abs(p1[1] - dp[1])
print(d)

