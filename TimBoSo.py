import math
inp = input("Nhập số nguyên N: ")
N = int(inp)
abs_N = abs(N)
min_c = 1000000000000
for i in range(1, int(math.isqrt(abs_N)) + 1):
    if abs_N % i == 0:
        j = abs_N // i
        if N > 0:
            c1 = abs(i - j)
            min_c = min(min_c, c1)
        else:
            c2 = abs(i + j)
            min_c = min(min_c, c2)
print(min_c)
