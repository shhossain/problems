runs = int(input())

def squre_string(string:str) -> bool:
    chars = []
    for n,char in enumerate(string):
        if char not in chars:
            chars.append(char)
        else:
            nchar = string[0:n]
            if string.count(nchar) == 2:
                if (nchar + nchar) == string:
                    return True
            break
    return False

for i in range(runs):
    string = input()
    if squre_string(string):
        print('YES')
    else:
        print('NO')
    