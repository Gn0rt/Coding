import time
A = int(input())

start = time.time()
def gia_tri_lon_nhat(ds):
    lon_nhat = ds[0]
    for i in range(len(ds)):
        if ds[i] > lon_nhat:
            lon_nhat = ds[i]
    return lon_nhat

tong = A + A
hieu = A - A
tich = A * A

tap_hop = [tich, tong, hieu]
ket_qua = gia_tri_lon_nhat(tap_hop)
print(ket_qua)
end = time.time()
print(f"Thời gian chay: {end - start} giây")
