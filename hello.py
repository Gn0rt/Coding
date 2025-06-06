import sys


def main():
    # Fast I/O
    input_buffer = sys.stdin.readline

    # Read input
    n, q = map(int, input_buffer().strip().split())
    a = [0] + list(map(int, input_buffer().strip().split()))

    # Detect test case type based on first query
    test_queries = []
    for _ in range(q):
        l, r, x, y = map(int, input_buffer().strip().split())
        test_queries.append((l, r, x, y))

    if q == 0:
        print(" ".join(["0"] * n))
        return

    # Check if this is a small test case (n, q ≤ 10^3)
    if n <= 1000 and q <= 1000:
        # For small test cases, use direct approach
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            for l, r, x, y in test_queries:
                if l <= i <= r and a[i] % x == 0:
                    ans[i] += y
        print(" ".join(map(str, ans[1:n + 1])))
        return

    # Check if all queries have x = 1 or x ≤ 2
    x_values = set(query[2] for query in test_queries)
    if max(x_values) <= 2:
        # Simple case: only need to check if number is odd or even
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            for l, r, x, y in test_queries:
                if l <= i <= r:
                    if x == 1 or (x == 2 and a[i] % 2 == 0):
                        ans[i] += y
        print(" ".join(map(str, ans[1:n + 1])))
        return

    # Check if all queries are global (l=1, r=n)
    all_global = all(query[0] == 1 and query[1] == n for query in test_queries)
    if all_global:
        # For global updates, precompute once for each number
        value_updates = {}  # Maps each unique value to its total update
        for _, _, x, y in test_queries:
            for i in range(1, n + 1):
                if a[i] % x == 0:
                    value_updates[a[i]] = value_updates.get(a[i], 0) + y

        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = value_updates.get(a[i], 0)
        print(" ".join(map(str, ans[1:n + 1])))
        return

    # General case with optimized divisor calculation
    mx = max(a)
    ans = [0] * (n + 1)

    # Count frequency of each number
    num_freq = {}
    for i in range(1, n + 1):
        num_freq[a[i]] = num_freq.get(a[i], 0) + 1

    # Only compute divisors for numbers that actually appear in the array
    unique_nums = set(a[1:])
    divisors = {num: [] for num in unique_nums}

    for num in unique_nums:
        # Compute divisors efficiently
        i = 1
        while i * i <= num:
            if num % i == 0:
                divisors[num].append(i)
                if i != num // i:
                    divisors[num].append(num // i)
            i += 1

    # Process queries with difference array approach
    diff = [0] * (mx + 1)
    queries = [[] for _ in range(n + 2)]

    for l, r, x, y in test_queries:
        queries[l].append((x, y))
        queries[r + 1].append((x, -y))

    for i in range(1, n + 1):
        # Update frequencies
        for x, y in queries[i]:
            diff[x] += y

        # Calculate answer based on the current value's divisors
        current_val = a[i]
        for div in divisors[current_val]:
            ans[i] += diff[div]

    print(" ".join(map(str, ans[1:n + 1])))


if __name__ == "__main__":
    main()