matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matrix)

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

transposed = list(zip(*matrix))
print(transposed)

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))

print(matrix)
print(*matrix)  # Equivalent to: print(matrix[0], matrix[1], matrix[2])
print(matrix[0], matrix[1], matrix[2])
# as_tuples = *matrix  # SyntaxError: can't use starred expression here
