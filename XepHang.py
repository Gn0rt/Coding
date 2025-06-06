with open("POSMIN.INP", "r") as f:
    N = int(f.readline())
    A = list(map(int, f.readline().split()))
    Q = int(f.readline())
    queries = [int(f.readline()) for _ in range(Q)]

#Tạo mảng pos[v] lưu vị trị nhỏ nhất của giá trị v
M = max(A) #giá trị chiều cao lớn nhất
pos = [N+1]*(M+1) #Khởi tạo pos[v] = N+1 (không tồn tại)
for i in range(N):
    for v in range(A[i], M+1):
        pos[v] = min(pos[v], i+1)
with open("POSMIN.OUT", "w") as f:
    for k in queries:
        if k > M:
            result = pos[M] #Nếu k lớn hơn max(A), lấy vị trí nhỏ nhất của M
        else:
            result = pos[k] #vị trí nhỏ nhất có ạ <= k
        f.write(str(result) + '\n')

