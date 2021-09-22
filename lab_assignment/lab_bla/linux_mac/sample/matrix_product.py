matrix_a = [[1,1,2], [2,1,1]]
matrix_b = [[1,1], [2,1], [1,3]]

result = [[sum(a * b for a, b in zip(row_a, column_b)) 
            for column_b in zip(*matrix_b)] 
                for row_a in matrix_a]

print(result)

def vector_addition(*args):
    print(args)
    return [t for t in zip(*args)]

print(vector_addition([1,2],[2,3],[3,4]))
