# ABC174C - Repsept
# https://atcoder.jp/contests/abc174/tasks/abc174_c
k = int(input())


def seven():
    a = 7
    for i in range(k):
        a = a % k
        if a == 0:
            return i+1
        else:
            a = a*10+7
    return -1


print(seven())
