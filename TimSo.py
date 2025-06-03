import math

N = int(input())
X = int(input())

# Tìm phần không phải chính phương trong X (tức là tích các thừa số lẻ)
B = 1
tmp_X = X
i = 2
while i * i <= tmp_X:
    cnt = 0
    while tmp_X % i == 0:
        tmp_X //= i
        cnt += 1
    if cnt % 2 == 1:
        B *= i
    i += 1
if tmp_X > 1:  # tmp_X là số nguyên tố lớn hơn sqrt(X)
    B *= tmp_X

# Số lượng t thỏa mãn: t^2 <= N/B
if B > N:
    print(0)
else:
    max_t = int(math.isqrt(N // B))
    print(max_t)