import time


def sum_of_squares(n):
    """Return 0**2 + 1**2 + ... + (n-1)**2 in O(1) using the closed form
    (n-1) * n * (2n-1) / 6 instead of looping n times."""
    return (n - 1) * n * (2 * n - 1) // 6


def slow_function():
    # time.sleep(2) simulates unavoidable I/O wait, so it is kept.
    time.sleep(2)
    return sum_of_squares(10000)


def optimized_fast_function():
    return sum(i**2 for i in range(100))


def optimized_memory_intensive_function():
    # 10,000,000 Python-level iterations replaced by one formula.
    return sum_of_squares(10000000)


def main():
    slow_function()
    optimized_fast_function()
    optimized_memory_intensive_function()


if __name__ == "__main__":
    main()
