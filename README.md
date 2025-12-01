# Sorting Algorithms Benchmark

This document provides benchmark results comparing several sorting algorithms implemented in Python.

## Algorithms Tested

The following algorithms were included in the benchmark:

- **Insertion Sort** – simple quadratic-time algorithm, efficient only for small inputs.
- **Merge Sort** – classic divide-and-conquer algorithm with O(n log n) complexity.
- **Custom TimSort implementation** – hybrid algorithm combining Merge Sort and Insertion Sort.
- **Python built-in `sorted()`** – highly optimized reference implementation (real TimSort in C).

## Benchmark Methodology

All measurements were performed using the Python `timeit` module.

- Each algorithm was executed **5 times** per test case.
- Execution time was averaged across runs.
- All tests used randomly generated integer arrays.

### Input Sizes

The following array sizes were used:

```
50
100
1 000
5 000
10 000
```

## Summary of Results

- **Insertion Sort** is fast only for very small inputs.  
  Its O(n²) complexity causes significant slowdown starting at ~1k elements.

- **Merge Sort** demonstrates stable and predictable performance for all input sizes thanks to O(n log n) complexity.

- **Custom TimSort** generally performs better than Merge Sort, especially on partially sorted data.  
  This is expected due to the algorithm’s hybrid design.

- **Built-in `sorted()`** is consistently the fastest across all tests.  
  It is implemented in optimized C code and uses the production-grade TimSort.

## Conclusions

- These benchmarks are useful for understanding algorithmic behavior and comparing practical performance.
- For real-world usage, Python’s built-in `sorted()` should always be preferred.
- TimSort remains the most efficient general-purpose sorting algorithm for typical data patterns.
