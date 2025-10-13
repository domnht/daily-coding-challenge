# File Storage

Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

- The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
- Return the number of whole files the drive can fit.
- Use the following conversions:

| Unit | Equivalent |
|:----:|:----------:|
| 1 B  | 1 B        |
| 1 KB | 1000 B     |
| 1 MB | 1000 KB    |
| 1 GB | 1000 MB    |

For example, given `500`, `"KB"`, and `1` as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.

## Tests

1. `number_of_files(500, "KB", 1)` should return `2000`.
2. `number_of_files(50000, "B", 1)` should return `20000`.
3. `number_of_files(5, "MB", 1)` should return `200`.
4. `number_of_files(4096, "B", 1.5)` should return `366210`.
5. `number_of_files(220.5, "KB", 100)` should return `453514`.
6. `number_of_files(4.5, "MB", 750)` should return `166666`.

## Solution

```python
def number_of_files(file_size, file_unit, drive_size_gb):

    return file_size
```
