import time
import memory_profiler
import unittest
import profiler
from profiler import slow_function, optimized_fast_function, optimized_memory_intensive_function


class TestProfiler(unittest.TestCase):

    def time_function(self, func):
        """Times the execution of a function."""
        start_time = time.time()
        func()  # Execute the function
        end_time = time.time()
        return end_time - start_time

    def test_slow_function(self):
        """Test the slow_function for execution time."""
        duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.2f} seconds.")
        self.assertGreater(duration, 2, "slow_function should take more than 2 seconds.")

    def test_fast_function(self):
        """Test the fast_function for execution time."""
        duration = self.time_function(optimized_fast_function)
        print(f"optimized_fast_function executed in {duration:.2f} seconds.")
        self.assertLess(duration, 1, "fast_function should take less than 1 second.")

    def test_memory_intensive_function(self):
        """Test the memory_intensive_function and monitor memory usage."""
        mem_usage_before = memory_profiler.memory_usage()
        duration = self.time_function(optimized_memory_intensive_function)
        mem_usage_after = memory_profiler.memory_usage()

        print(f"optimized_memory_intensive_function executed in {duration:.2f} seconds.")
        print(f"Memory usage before: {mem_usage_before[0]:.2f} MiB, after: {mem_usage_after[0]:.2f} MiB.")

        self.assertLess(duration, 5, "memory_intensive_function should take less than 5 seconds.")
        # After optimization the function no longer loops/allocates, so memory
        # is expected to stay flat (the original test required it to grow).
        self.assertLessEqual(mem_usage_after[0] - mem_usage_before[0], 1,
                             "Optimized function should not increase memory usage noticeably.")


    def test_results_unchanged(self):
        """The optimized functions must return the same values as the originals."""
        self.assertEqual(slow_function(), sum(i ** 2 for i in range(10000)))
        self.assertEqual(optimized_fast_function(), 328350)
        self.assertEqual(optimized_memory_intensive_function(), 333333283333335000000)

    def test_main(self):
        """main() runs all three functions without error."""
        self.assertIsNone(profiler.main())


def main():
    unittest.main()


if __name__ == "__main__":
    main()
