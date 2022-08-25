# interesting_sum
def interesting_sum(lst:list) -> int:
    sort_lst = sorted(lst)
    return sort_lst[-1] + sort_lst[-2] - sort_lst[0] - sort_lst[1]

runs = int(input())
for i in range(runs):
    n = int(input())
    lst = list(map(int, input().split()))
    print(interesting_sum(lst))

