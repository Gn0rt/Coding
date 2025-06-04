# Hàm tính giai thừa của n (n!)
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Hàm tính tổ hợp C(n, k)
def combination(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

# Đọc dữ liệu đầu vào
m, n, k, l = map(int, input().split())  # m: số hàng, n: số cột, k: số xe trắng, l: số xe đen

# Tính số cách đặt quân xe an toàn
# Bước 1: Chọn k hàng từ m hàng cho xe trắng: C(m, k)
ways_white_rows = combination(m, k)

# Bước 2: Chọn k cột từ n cột cho xe trắng: C(n, k)
ways_white_cols = combination(n, k)

# Bước 3: Đặt k quân xe trắng vào k hàng và k cột (mỗi hàng/cột chỉ 1 quân): k!
ways_white_place = factorial(k)

# Bước 4: Chọn l hàng từ (m-k) hàng còn lại cho xe đen: C(m-k, l)
ways_black_rows = combination(m - k, l)

# Bước 5: Chọn l cột từ (n-k) cột còn lại cho xe đen: C(n-k, l)
ways_black_cols = combination(n - k, l)

# Bước 6: Đặt l quân xe đen vào l hàng và l cột: l!
ways_black_place = factorial(l)

# Tổng số cách = số cách chọn hàng/cột cho trắng * số cách đặt trắng * số cách chọn hàng/cột cho đen * số cách đặt đen
total_ways = (ways_white_rows * ways_white_cols * ways_white_place *
              ways_black_rows * ways_black_cols * ways_black_place)

# In kết quả
print(total_ways)