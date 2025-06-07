# Đọc input từ file GTBT.INP
with open("GTBT.INP", "r") as f:
    T = int(f.readline())  # Số test
    tests = [f.readline().strip() for _ in range(T)]  # Đọc T biểu thức


# Hàm tính giá trị biểu thức a?b?c
def eval_expr(s):
    a = int(s[0])  # Số thứ nhất
    op1 = s[1]  # Toán tử thứ nhất
    b = int(s[2])  # Số thứ hai
    op2 = s[3]  # Toán tử thứ hai
    c = int(s[4])  # Số thứ ba

    # Tính (a op1 b)
    if op1 == '+':
        x = a + b
    else:  # op1 == '*'
        x = a * b

    # Tính (x op2 c)
    if op2 == '+':
        result = x + c
    else:  # op2 == '*'
        result = x * c

    return result


# Ghi output ra file GTBT.OUT
with open("GTBT.OUT", "w") as f:
    for s in tests:
        result = eval_expr(s)
        f.write(str(result) + '\n')