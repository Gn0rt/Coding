with open("POSMIN.INP", "r") as f:
    N = int(f.readline())
    A = list(map(int, f.readline().split()))
    Q = int(f.readline())
    queries = [int(f.readline()) for _ in range(Q)]

# Tạo dictionary pos[v] lưu vị trí nhỏ nhất của giá trị v
pos = {}  # Lưu vị trí nhỏ nhất (1-based)
for i in range(N):
    v = A[i]
    if v not in pos or i + 1 < pos[v]:
        pos[v] = i + 1  # Cập nhật vị trí nhỏ nhất

# Tạo danh sách giá trị duy nhất và sắp xếp
values = sorted(pos.keys())  # Các giá trị v xuất hiện trong A
m = len(values)  # Số giá trị duy nhất

# Tiền xử lý: Lưu vị trí nhỏ nhất cho giá trị <= v
min_pos = [N + 1] * m  # Lưu vị trí nhỏ nhất cho mỗi values[i]
min_pos[0] = pos[values[0]]
for i in range(1, m):
    min_pos[i] = min(min_pos[i-1], pos[values[i]])  # Kéo vị trí nhỏ nhất

for k in queries:
    # Tìm giá trị lớn nhất <= k trong values bằng tìm kiếm nhị phân
    left, right = 0, m - 1
    result = N + 1
    while left <= right:
        mid = (left + right) // 2
        if values[mid] <= k:
            result = min(result, min_pos[mid])
            left = mid + 1  # Tìm tiếp ở nửa phải
        else:
            right = mid - 1  # Tìm ở nửa
    print(f"result = {result}")
# with open("POSMIN.OUT", "w") as f:
#     for k in queries:
#         if k > M:
#             result = pos[M] #Nếu k lớn hơn max(A), lấy vị trí nhỏ nhất của M
#         else:
#             result = pos[k] #vị trí nhỏ nhất có ạ <= k
#         f.write(str(result) + '\n')

