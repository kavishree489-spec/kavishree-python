from functools import lru_cache

# Plain recursion

calls = 0

def ways_naive(n):

    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n-1) + ways_naive(n-2)


calls = 0

print("Ways:", ways_naive(5))
print("Function calls:", calls)


# Memoisation

calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):

    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n-1) + ways_memo(n-2)


calls = 0

print("Memoised ways:", ways_memo(25))
print("Function calls:", calls)


# Iterative method

def ways_loop(n):

    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):

        c = a + b

        a = b
        b = c

    return b


print("Ways for 1000 steps:", ways_loop(1000))