from module_test import do_test

def find_landing_spot(matrix: list) -> list:
    min = -1
    target_i = -1
    target_j = -1

    height = len(matrix)
    width = len(matrix[0])

    for i in range(0, height):
        for j in range(0, width):
            # Check if current position is 0
            if matrix[i][j] > 0: continue

            # Caculate sum of (up to) 4 neighbors
            sum = matrix[i][j]
            if i - 1 >= 0:     sum += matrix[i - 1][j]
            if i + 1 < height: sum += matrix[i + 1][j]
            if j - 1 >= 0:     sum += matrix[i][j - 1]
            if j + 1 < width:  sum += matrix[i][j + 1]

            # Compare and assign new min value
            if min == -1 or min > sum:
                target_i = i
                target_j = j
                min = sum

    return [target_i, target_j]

do_test(function_name="find_landing_spot", should_return=[0, 1], matrix=[[1, 0], [2, 0]])
do_test(function_name="find_landing_spot", should_return=[1, 1], matrix=[[9, 0, 3], [7, 0, 4], [8, 0, 5]])
do_test(function_name="find_landing_spot", should_return=[2, 2], matrix=[[1, 2, 1], [0, 0, 2], [3, 0, 0]])
do_test(function_name="find_landing_spot", should_return=[2, 1], matrix=[[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]])
