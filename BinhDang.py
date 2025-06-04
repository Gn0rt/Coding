# Đọc dữ liệu đầu vào
n, k = map(int, input().split())  # n: độ dài xâu, k: số chữ cái (A đến K)
s = input()  # Xâu s chứa n chữ cái viết hoa

# Đếm tần suất của mỗi chữ cái (A đến K)
freq = [0] * k  # Mảng tần suất: freq[0] cho A, freq[1] cho B, ...
for char in s:
    # Chuyển chữ cái thành chỉ số: A -> 0, B -> 1, ..., K -> k-1
    index = ord(char) - ord('A')
    freq[index] += 1
print(freq)
# Tìm t tối đa có thể (tần suất nhỏ nhất của k chữ cái)
max_t = min(freq)  # t không thể lớn hơn tần suất nhỏ nhất

# Hàm kiểm tra xem có dãy con tốt với mỗi chữ cái xuất hiện t lần không
def can_make_good_substring(t):
    # Nếu t = 0, dãy con rỗng luôn tốt
    if t == 0:
        return True
    # Kiểm tra xem mỗi chữ cái có xuất hiện ít nhất t lần không
    for i in range(k):
        if freq[i] < t:  # Nếu một chữ cái không đủ t lần
            return False
    return True  # Nếu tất cả chữ cái đều đủ t lần, dãy con tốt tồn tại
# Hàm kiểm tra xem có dãy con tốt với mỗi chữ cái xuất hiện t lần không
def can_make_good_substring1(t):
    if t == 0:
        return True
    # Dùng cửa sổ trượt để tìm đoạn có ít nhất t lần mỗi chữ cái
    for i in range(n):  # Vị trí bắt đầu
        count = [0] * k  # Đếm tần suất trong cửa sổ
        for j in range(i, n):  # Vị trí kết thúc
            index = ord(s[j]) - ord('A')
            count[index] += 1
            # Kiểm tra xem tất cả k chữ cái có ít nhất t lần không
            all_enough = True
            for c in range(k):
                if count[c] < t:
                    all_enough = False
                    break
            if all_enough:
                return True  # Tìm thấy đoạn thỏa mãn
    return False

# Tìm kiếm nhị phân để tìm t lớn nhất
left = 0  # t nhỏ nhất
right = max_t  # t lớn nhất
best_t = 0  # t tốt nhất tìm được

while left <= right:
    mid = (left + right) // 2  # Thử t = mid
    if can_make_good_substring(mid):
        best_t = mid  # Nếu mid khả thi, thử t lớn hơn
        left = mid + 1
    else:
        right = mid - 1  # Nếu không khả thi, thử t nhỏ hơn

# Độ dài dãy con tốt dài nhất là t * k
result = best_t * k
print(result)