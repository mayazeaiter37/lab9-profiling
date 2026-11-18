from memory_profiler import profile
import time


def sum_of_squares(n):
    return (n - 1) * n * (2 * n - 1) // 6


@profile
def slow_function():
    time.sleep(2)
    return sum_of_squares(10000)


@profile
def optimized_fast_function():
    return sum(i**2 for i in range(100))


@profile
def optimized_memory_intensive_function():
    return sum_of_squares(10000000)


def main():
    slow_function()
    optimized_fast_function()
    optimized_memory_intensive_function()


if __name__ == "__main__":
    main()
