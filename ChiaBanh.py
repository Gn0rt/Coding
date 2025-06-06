import time
start_time = time.time()
with open('CAKES.INP', 'r') as f:
    N = int(f.readline())
uoc_nho = []
uoc_lon = []
i = 1
while i * i <= N:
    if N % i == 0:
        uoc_nho.append(i)
        if i * i != N:
            uoc_lon.append(N // i)
    i += 1
end_time = time.time()
tg = end_time - start_time
with open('CAKES.OUT', 'w') as f:
    for k in reversed(uoc_lon):
        f.write(f"{k} \n")
    f.write(f"{tg}")



