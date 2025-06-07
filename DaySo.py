from collections import deque

# Đọc input
# n, L, R = map(int, input().split())
# A = list(map(int, input().split()))
n = 5
L = 2
R = 3
A = [1, 3, -1, 5, -1]
# Tính tổng tiền tố
P = [0] * (n + 1)
for i in range(n):
    P[i + 1] = P[i] + A[i]

# Tìm tổng lớn nhất của dãy con dài từ L đến R
max_sum = float('-inf')
for s in range(L, R + 1):  # Duyệt độ dài s
    d = deque()  # Deque lưu chỉ số của P[j]
    for i in range(n + 1):  # Duyệt chỉ số i
        # Loại bỏ các chỉ số ngoài cửa sổ [i-s, i]
        while d and d[0] < i - s:
            d.popleft()
        # Loại bỏ các P[j] lớn hơn P[i], vì không tối ưu
        while d and P[d[-1]] >= P[i]:
            d.pop()
        d.append(i)
        # Nếu i >= s, tính tổng đoạn [j, i-1] với j là chỉ số min
        if i >= s:
            max_sum = max(max_sum, P[i] - P[d[0]])

# In kết quả
print(max_sum)