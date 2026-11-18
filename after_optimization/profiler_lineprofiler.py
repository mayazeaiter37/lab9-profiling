import time

from line_profiler import LineProfiler


def profile_main():
    profiler = LineProfiler()
    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(optimized_memory_intensive_function)
    profiler.runcall(main)
    profiler.print_stats()


def sum_of_squares(n):
    return (n - 1) * n * (2 * n - 1) // 6


def slow_function():
    time.sleep(2)
    return sum_of_squares(10000)


def optimized_fast_function():
    return sum(i**2 for i in range(100))


def optimized_memory_intensive_function():
    return sum_of_squares(10000000)


def main():
    slow_function()
    optimized_fast_function()
    optimized_memory_intensive_function()


if __name__ == "__main__":
    profile_main()
