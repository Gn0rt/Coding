import math

N = int(input("Nhập N: "))  # Ví dụ: 40
X = int(input("Nhập X: "))  # Ví dụ: 12

print(f"\nBước 1: Phân tích X = {X} ra thừa số nguyên tố.")

tmp_X = X
B = 1
i = 2
while i * i <= tmp_X:
    cnt = 0
    while tmp_X % i == 0:
        tmp_X //= i
        cnt += 1
    if cnt > 0:
        print(f"  - Thừa số {i} xuất hiện {cnt} lần.")
    if cnt % 2 == 1:
        B *= i
        print(f"    -> Số mũ lẻ, nhân {i} vào B (B hiện tại: {B})")
    i += 1
if tmp_X > 1:
    B *= tmp_X
    print(f"  - Thừa số {tmp_X} xuất hiện 1 lần. Số mũ lẻ, nhân vào B (B hiện tại: {B})")

print(f"\nKết quả phân tích: B = {B} (Tích các thừa số nguyên tố với số mũ lẻ)")

if B > N:
    print(f"B = {B} lớn hơn N = {N} ⇒ Không có Y nào thỏa mãn.")
    print(0)
else:
    print(f"\nBước 2: Tìm các giá trị t sao cho Y = B * t^2 ≤ N")
    max_t = int(math.isqrt(N // B))
    print(f"  - Tìm t nguyên dương ≤ sqrt(N/B) = sqrt({N}//{B}) = {max_t}")
    print(f"  - Các giá trị t thỏa mãn: ", end="")
    for t in range(1, max_t + 1):
        Y = B * t * t
        print(f"{t} (Y = {B}*{t}^2 = {Y})", end=", ")
    print(f"\n\nSố lượng Y hợp lệ là: {max_t}")
    print(max_t)