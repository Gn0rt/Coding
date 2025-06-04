import sys
from collections import defaultdict

def main():
    # Read N and Q
    N, Q = map(int, sys.stdin.readline().split())

    # Read student codes
    a = list(map(int, sys.stdin.readline().split()))

    # Read queries and group by x
    events = defaultdict(list)
    for _ in range(Q):
        parts = sys.stdin.readline().split()
        l = int(parts[0]) - 1
        r = int(parts[1]) - 1
        x = int(parts[2])
        v = int(parts[3])
        events[x].append((l, r, v))

    # Build all divisors for numbers up to max_a
    max_a = max(a)
    divisors = [[] for _ in range(max_a + 1)]
    for d in range(1, max_a + 1):  # d là ước
        for m in range(d, max_a + 1, d):  # m là bội của d
            divisors[m].append(d)

    # Difference array
    delta = [0] * (N + 1)

    # Apply all queries via divisor matching
    for i in range(N):
        ai = a[i]
        for x in divisors[ai]:  # x là ước của ai
            for (l, r, v) in events[x]:
                delta[l] += v
                if r + 1 < N:
                    delta[r + 1] -= v
                else:
                    delta[r + 1] -= v  # vẫn giữ để đảm bảo logic

    # Compute prefix sum
    res = []
    curr = 0
    for i in range(N):
        curr += delta[i]
        res.append(str(curr))

    print(' '.join(res))

if __name__ == "__main__":
    main()