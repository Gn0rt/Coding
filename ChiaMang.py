from array import array
N = int(input())
A = array('i', map(int, input().split()))
#'q' là kiểu int64, trán tràn với số lớn
sumArr = array('q', [0] * (N+1))

print(f"Before: sumArr = {sumArr}")
for i in range(1, N+1):
    print(f"sumArr[{i}] = {sumArr[i-1]} + {A[i-1]}")
    sumArr[i] = sumArr[i - 1] + A[i - 1]
print(f"After: sumArr = {sumArr}")
print("-------||-------")
count = 0
#duyệt tất cả dãy con liên tiếp [l,r]
for l in range(N):
    print(f"l = {l}")
    for r in range(l,N):
        print(f"r = {r}")
        #kiểm tra đoạn [l,r] có tồn tại vị trí x thỏa mãn yêu cầu
        found = False
        for x in range(l, r+1):
            #tổng từ l -> x
            sum_left = sumArr[x+1] - sumArr[l]
            print(f"sum_left = sumArr[{x+1}] - sumArr[{l}] = {sumArr[x+1] - sumArr[l]}")
            #tổng từ x -> r
            sum_right = sumArr[r+1] - sumArr[x]
            print(f"sum_right = sumArr[{r+1}] - sumArr[{x}] = {sumArr[r+1] - sumArr[x]}")
            print("--------------")
            if sum_left == 0 and sum_right == 0:
                found = True
                break
        if found:
            count += 1

print(count)
