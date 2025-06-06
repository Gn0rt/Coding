import math
with open('CNTSEQ.INP', 'r') as f:
    n, S = map(int, f.readline().split())
    A = list(map(int, f.readline(). split()))
print(f"n = {n}\nS = {S}\nA = {A}")
# Cách 1: Chưa tối ưu
# B = []
# for i in range(n):
#     total = 0
#     for j in range(i,n):
#         total += A[j]
#         B.append(total)
#
# count = 0
# for i in range(len(B)):
#     if abs(B[i]) > S:
#         count += 1
# print(count)

#Cách 2: Tối ưu hơn cách 1
# Tính mảng tổng tiền tố
P = [0] * (n + 1)  # P[0] = 0, P[i] = a_1 + a_2 + ... + a_i
for i in range(n):
    print(f"P[{i+1}] = P[{i}] + A[{i}]")
    P[i + 1] = P[i] + A[i]  # Tổng tiền tố đến vị trí i
    print(f"P[{i+1}] = {P[i+1]}")

print(P)
# Tạo danh sách (tổng tiền tố, chỉ số) để sắp xếp
P_with_index = [(P[i], i) for i in range(n + 1)]  # Lưu (giá trị, chỉ số)
P_with_index.sort()  # Sắp xếp theo giá trị tổng tiền tố

print(P_with_index)
count = 0
for i in range(n + 1):  # Duyệt từng P[i-1]
    left = 0  # Con trỏ trái
    right = n  # Con trỏ phải
    target = P[i]  # Giá trị P[i-1] (lấy từ P gốc, i là i-1 trong công thức)

    # Tìm các P[j] < target - S
    while left <= right:
        mid = (left + right) // 2
        print(f"left = {left}\nright = {right}\nmid = {mid}")
        if mid >= n + 1:
            right = mid - 1
            continue
        print(f"{P_with_index[mid][0]} < {target} - {S} and {P_with_index[mid][1]} >= {i}")
        if P_with_index[mid][0] < target - S and P_with_index[mid][1] >= i:
            left = mid + 1
        else:
            right = mid - 1
    count += left  # Số cặp P[j] < target - S với j >= i
    print("--------------------------" * 2)
    # Tìm các P[j] > target + S
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        print(f"left = {left}\nright = {right}\nmid = {mid}")
        if mid >= n + 1:
            right = mid - 1
            continue
        print(f"{P_with_index[mid][0]} > {target} + {S} and {P_with_index[mid][1]} >= {i}")
        if P_with_index[mid][0] > target + S and P_with_index[mid][1] >= i:
            right = mid - 1
        else:
            left = mid + 1
    count += n - right  # Số cặp P[j] > target + S với j >= i

with open("CNTSEQ.OUT", 'w') as f:
    f.write(str(count))
