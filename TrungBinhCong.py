from bisect import bisect_left

# Đọc input
N, T = map(int, input().split())
A = list(map(int, input().split()))

# Tạo mảng B: (giá trị, chỉ số), sắp xếp theo giá trị
B = [(a, i + 1) for i, a in enumerate(A)]  # Chỉ số 1-based
B.sort()

# Tìm bộ ba có trung bình gần T nhất
min_diff = float('inf')  # Chênh lệch nhỏ nhất
max_sum = float('-inf')  # Tổng lớn nhất khi chênh lệch min
target = 3 * T  # Mục tiêu: A_i + A_j + A_k ≈ 3T

for j in range(1, N):  # Chỉ số j (1-based)
    for k in range(j + 1, N + 1):  # Chỉ số k (1-based)
        # Tìm A_i sao cho A_i + A_j + A_k ≈ 3T
        target_i = target - (A[j - 1] + A[k - 1])  # A_i ≈ 3T - (A_j + A_k)

        # Tìm kiếm nhị phân A_i gần target_i nhất, với i < j
        idx = bisect_left(B, (target_i, 0))  # Tìm vị trí chèn target_i

        # Kiểm tra các giá trị gần target_i
        for pos in [idx, idx - 1]:  # Kiểm tra cả bên trái và bên phải
            if 0 <= pos < N:
                val_i, i = B[pos]
                if i < j:  # Đảm bảo i < j < k
                    S = val_i + A[j - 1] + A[k - 1]
                    diff = abs(S - target)  # Chênh lệch |S - 3T|
                    if diff < min_diff:
                        min_diff = diff
                        max_sum = S
                    elif diff == min_diff:
                        max_sum = max(max_sum, S)

# In kết quả: Tổng của bộ ba
print(max_sum)