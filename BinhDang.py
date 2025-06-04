n, k = map(int, input())
s = input()

freq = [0] * k
for char in s:
    index = ord(char) - ord('A')
    freq[index] += 1

min_freq = min(freq)
result = min_freq * k
print(result)