# quee_at_school

# GBBGBB

chars,n = list(map(int,input().split()))
string = input()
while n:
    string = string.replace("BG","GB")
    n -= 1
print(string)