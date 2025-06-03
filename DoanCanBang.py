n = 7
lists = [-1, 2, 1, 0, -3, -1, 1]
newlists = [0] * n

for L in range(n):
    tong = 0
    print(f"L = {L}")
    for R in range(L, n):
        print(f"R = {R}")
        print(f"Tong = {tong} + {lists[R]}")
        tong += lists[R]
        print(f"Tong = {tong}")
        print("-------")
        if tong == 0:
            for i in range(L, R+1):
                newlists[i] += 1
                print(f"Số {lists[i]} xuất hiện: {newlists[i]} lần")

print(newlists)




