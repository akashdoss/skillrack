def count_ones(matrix, col_idx):
    return sum(matrix[row_idx][col_idx] for row_idx in range(len(matrix)))

def count_consecutive_zeros_at_bottom(matrix, col_idx):
    count = 0
    for row_idx in reversed(range(len(matrix))):
        if matrix[row_idx][col_idx] == 0:
            count += 1
        else:
            break
    return count

def sort_columns_by_conditions(matrix, R, C):
    columns_info = []

    for col_idx in range(C):
        num_ones = count_ones(matrix, col_idx)
        consecutive_zeros = count_consecutive_zeros_at_bottom(matrix, col_idx)
        columns_info.append((num_ones, consecutive_zeros, col_idx))
    
    columns_info.sort(key=lambda x: (-x[0], -x[1], x[2]))

    sorted_matrix = []
    for row_idx in range(R):
        sorted_row = [matrix[row_idx][col_idx] for _, _, col_idx in columns_info]
        sorted_matrix.append(sorted_row)

    for row in sorted_matrix:
        print(" ".join(map(str, row)))

R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

sort_columns_by_conditions(matrix, R, C)
