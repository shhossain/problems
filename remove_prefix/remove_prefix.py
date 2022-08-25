def duplicate_val(lst:list) -> int:
    lst_set = set(lst)
    print(lst,lst_set)
    return len(lst) - len(lst_set)

runs = int(input())
for i in range(runs):
    n = int(input())
    lst = list(map(int, input().split()))
    print(duplicate_val(lst))

