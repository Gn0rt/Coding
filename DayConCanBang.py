with open('BALANSEQ.INP', 'r') as f:
    n = int(f.readline()) # đọc số lượng phần tử
    A = list(map(int, f.readline().split())) #Đọc dãy số A

sum_dict = {0: -1}
current_sum = 0
max_length = 0

#Duyệt từng phần tử của dãy
for i in range(n):
    #Gán +1 cho số dương, -1 cho số am, 0 cho số 0
    if A[i] > 0:
        current_sum += 1
    elif A[i] < 0:
        current_sum -= 1
    #A[i] = 0, không thay đổi

    #Kiểm tra xem tổng hiện tại đã xuất hiện trước đó chưa
    if current_sum in sum_dict:
        print(f"Lần thứ {i + 1}")
        #Nếu có, dãy con từ sum_dict[current_sum] + 1 đến i có tổng 0
        print(f"length = {i} - {sum_dict[current_sum]}")
        length = i - sum_dict[current_sum] #độ dài dãy con
        print(f"length = {length}")
        max_length = max(max_length, length) #cập nhật độ dài lớn nhất
    else:
        print(f"Lần thứ {i + 1}")
        #lưu tổng hiện tại và chỉ số đầu tiên xuất hiện
        sum_dict[current_sum] = i
        print(f"sum_dict[{current_sum}] = {i}")
        print(f"sum_dict = {sum_dict}")

with open('BALANSEQ.OUT', 'w') as f:
    f.write(str(max_length))