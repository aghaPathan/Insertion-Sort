# Insertion Sort

A Python module implementing the Insertion Sort algorithm.

## Overview

Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

## Installation

```bash
pip install .
```

## Usage

```python
from insertion_sort import InsertionSort

sorter = InsertionSort()
result = sorter.sort([12, 11, 13, 5, 6])
print(result)  # [5, 6, 11, 12, 13]
```

## Algorithm Characteristics

- **Time Complexity:** O(n²) worst case, O(n) best case
- **Space Complexity:** O(1)
- **Stable:** Yes
- **In-place:** Yes
- **Adaptive:** Yes (efficient for nearly sorted data)

## How It Works

1. Start from second element
2. Compare with elements in sorted portion
3. Shift larger elements right
4. Insert element in correct position
5. Repeat for remaining elements

## Best For

- Small datasets
- Nearly sorted arrays
- Online sorting (data arrives sequentially)

## License

MIT
