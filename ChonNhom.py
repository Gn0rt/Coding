n = 9
k = 2

#lists = [1, 2, 3, 4, -2, 6, 7, 8, -9]
lists = [-100, -10, 3, 4, -2, 6, 7, 22, -9]
#-100 -10 -9 -2 3 4 6 7 22
lists.sort()

l = 0
r = n - 1
res = 0
for i in range(k):
    if r - 1 > l:
        prod1 = lists[r] * lists[r-1] * lists[r-2]
    else:
        prod1 = float('-inf')

    if l + 1 < r:
        prod2 = lists[l] * lists[l+1] * lists[r]
    else:
        prod2 = float('-inf')

    if prod1 >= prod2:
        res += prod1
        r -= 3
    else:
        res += prod2
        l += 2
        r -= 1

print(res)









