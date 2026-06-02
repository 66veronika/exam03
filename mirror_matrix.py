# Write a function that mirrors a 2D matrix horizontally by reversing each row.

def mirror_matrix(matrix: list[list[int]]):
    # return [row[::-1] for row in matrix]

    res = []
    for row in matrix:
        res.append(row[::-1])

    return res


lst = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3],
]

res = mirror_matrix(lst)
print(res)
