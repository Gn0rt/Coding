import itertools
m, n, k, l = map(int, input().split())

# Tạo danh sách tất cả các ô trên bàn cờ, mỗi ô là (hàng, cột)
cells = []
for row in range(m):
    for col in range(n):
        cells.append((row, col))

for white in itertools.combinations(cells, k):
    print(white)
    whites_set = set(white)
    remain_cells = [cell for cell in cells if cell not in whites_set]
    print(remain_cells)
    for black in itertools.combinations(remain_cells, l):
        print(black)
        antoan = True
        for wx, wy in white:
            print(f"{wx}, {wy}")