x = int(input())
y = int(input())
z = int(input())

numbers = [x,y,z]
max_value = None
result = None

for i in range(3):
    c = numbers[i]
    if c <= 0:
        continue
    if i == 0:
        a1, b1 = numbers[1], numbers[2]
        a2, b2 = numbers[2], numbers[1]
    elif i == 1:
        a1, b1 = numbers[0], numbers[2]
        a2, b2 = numbers[2], numbers[0]
    else:
        a1, b1 = numbers[0], numbers[1]
        a2, b2 = numbers[1], numbers[0]
    value1 = a1 + b1 / c
    if (max_value is None) or (value1 > max_value):
        max_value = value1
        result = (a1, b1, c)
    value2 = a2 + b2 /c
    if value2 > max_value:
        max_value = value28
        result = (a2, b2, c)
if result is not None:
    print(f"{result[0]} {result[1]} {result[2]}");
else:
    print(-1)
