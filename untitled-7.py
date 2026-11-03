import time

# Original recursive method

def ways_naive(n):

    if n <= 1:
        return 1

    return ways_naive(n-1) + ways_naive(n-2)


# Optimised iterative method

def ways_optimized(n):

    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):

        c = a + b

        a = b
        b = c

    return b


# Compare both methods

for n in [10, 20, 25, 30]:

    start = time.perf_counter()

    original = ways_naive(n)

    original_time = time.perf_counter() - start

    start = time.perf_counter()

    redesigned = ways_optimized(n)

    redesigned_time = time.perf_counter() - start

    print("\nn =", n)

    print("Original result:", original)

    print("Redesigned result:", redesigned)

    print("Same result:", original == redesigned)

    print("Original time:", original_time)

    print("Redesigned time:", redesigned_time)


# Operation count comparison

def ways_counted(n):

    calls = 0

    def calculate(n):

        nonlocal calls
        calls += 1

        if n <= 1:
            return 1

        return calculate(n-1) + calculate(n-2)

    answer = calculate(n)

    return answer, calls


def ways_loop_counted(n):

    additions = 0

    if n <= 1:
        return 1, additions

    a = 1
    b = 1

    for i in range(2, n + 1):

        c = a + b

        additions += 1

        a = b
        b = c

    return b, additions


for n in [10, 20, 25, 30]:

    result1, calls = ways_counted(n)

    result2, additions = ways_loop_counted(n)

    print("\nn =", n)
    print("Recursive calls:", calls)
    print("Loop additions:", additions)
    print("Same result:", result1 == result2)