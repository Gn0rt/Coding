with open("XAUDX.INP", 'r') as f:
    n = int(f.readline())
    strings = [f.readline().strip() for _ in range(n)]

alphabet = []
for i in range(ord('A'), ord('A')+26):
    alphabet.append(chr(i))
# Hàm kiêm tra đối xứng
# def doixung(xau):
#     l = 0
#     r = len(xau) - 1
#     while l <= r:
#         if xau[l] != xau[r]:
#             return False
#         l+=1
#         r-=1
#     return True
def chuyenxau(xau):
    xau_list = list(xau)
    left = 0
    right = len(xau) - 1
    while left <= right:
        # Trường hợp cả hai không phải '?' và khác nhau
        if xau_list[left] != '?' and xau_list[right] != '?' and xau_list[left] != xau_list[right]:
            return "-1"  # Không thể tạo xâu đối xứng
        elif xau_list[left] != '?' and xau_list[right] == '?':
            xau_list[right] = xau_list[left]
        elif xau_list[left] == '?' and xau_list[right] != '?':
            xau_list[left] = xau_list[right]
        elif xau_list[left] == '?' and xau_list[right] == '?':
            xau_list[left] = xau_list[right] = min(alphabet)
        left += 1
        right-=1
    return ''.join(xau_list)

with open("XAUDX.OUT", "w") as f:
    for s in strings:
        result = chuyenxau(s)
        f.write(result + '\n')
