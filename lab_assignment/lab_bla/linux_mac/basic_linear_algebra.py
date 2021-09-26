def vector_size_check(*vector_variables):
#    value = 0
#    last_value = 0
#    for vector in vector_variables:
#        value = len(vector)
#        if last_value == 0:
#            last_value = len(vector)
#        else:
#            if value != last_value:
#                return False
#    return True
    return len(set([len(vector) for vector in vector_variables])) == 1

#print(vector_size_check([1,2,3],[2,3,4],[5,6,7]))

#def vector_addition(*args):
#    print(args)
#    return [t for t in zip(*args)]

#print(vector_addition([1,2],[2,3],[3,4]))


def vector_addition(*vector_variables):
    #print(vector_variables)
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    ret = [ sum(vector) for vector in zip(*vector_variables)]
    

    print(ret)
    return ret

#vector_addition([1,3],[2,4],[6,7])
#vector_addition([1,5],[10,4],[4,7])
#vector_addition([1,3,4],[4],[6,7])

# args should be 1 dime list, tuple
def sub(args):
#    print("========")
#    print(args)
#    print(type(args))
#    print("========")
    #print(len(args))
    result = args[0]
    for i in range(1,len(args)):
        result -= args[i]
    return result

def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    ret = [ sub(vector) for vector in zip(*vector_variables)]
    print(ret)
    return ret

#vector_subtraction([1,3],[2,4])
#vector_subtraction([1,5],[10,4],[4,7])

def scalar_vector_product(alpha, vector_variable):

    result = []
    result = [alpha * vector for vector in vector_variable]
    print(result)
    return result

#scalar_vector_product(5,[1,2,3])
#scalar_vector_product(3,[2,2])
#scalar_vector_product(4,[1])

def matrix_size_check(*matrix_variables):
    #print(*matrix_variables);
    result = set([ (len(matrix), len(matrix_row)) for matrix in matrix_variables for matrix_row in matrix]) # Row 행, Column 열
    #print(result)
    return len(result) == 1 

#matrix_x = [[2,2], [2,3], [2,2]]
#matrix_y = [[2,5], [2,1]]
#matrix_z = [[2,4], [5,3]]
#matrix_w = [[2,5], [1,1], [2,2]]
#matrix_l = [[1,4], [2,5], [3,6]]
#matrix_o = [[10,40], [20,50], [30,60]]
#print(matrix_size_check(matrix_x, matrix_y, matrix_z))
#print(matrix_size_check(matrix_y, matrix_z))
#print(matrix_size_check(matrix_x, matrix_w))
#print(matrix_size_check(matrix_l, matrix_o))

def is_matrix_equal(*matrix_variables):
    
    for i in range(1, len(matrix_variables)):
        if matrix_variables[0] != matrix_variables[i]:
            return False
    return True

#matrix_x = [[2,2], [2,2]]
#matrix_y = [[2,5], [2,1]]

#print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y))
#print(is_matrix_equal(matrix_x, matrix_x))

def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    #print(*matrix_variables)
    #result =  [print(matrix_row) for matrix in zip(*matrix_variables) for matrix_row in zip(*matrix)]
    result =  [[sum(matrix_row) for matrix_row in zip(*matrix)] for matrix in zip(*matrix_variables)]
    return result

matrix_x = [[2,2], [2,2]]
matrix_y = [[2,5], [2,1]]
matrix_z = [[2,4], [5,3]]

#print(matrix_addition(matrix_x, matrix_y))
#print(matrix_addition(matrix_x, matrix_y, matrix_z))

def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    result =  [[sub(matrix_row) for matrix_row in zip(*matrix)] for matrix in zip(*matrix_variables)]
    return result

matrix_x = [[2,2], [2,2]]
matrix_y = [[2,5], [2,1]]
matrix_z = [[2,4], [5,3]]

#print(matrix_subtraction(matrix_x, matrix_y))
#print(matrix_subtraction(matrix_x, matrix_y, matrix_z))

def matrix_transpose(matrix_variable):
    #result = [matrix_row for matrix_row in zip(*matrix_variable)]
    #print(matrix_variable)
    #print(*matrix_variable)
    #print(zip(*matrix_variable))
    #print(list(zip(*matrix_variable)))
    #print(*list(zip(*matrix_variable)))
    result = [ [element for element in t] for t in zip(*matrix_variable)]
    return result

matrix_w = [[2,5],[1,1],[2,2]]
#print(matrix_transpose(matrix_w))

def scalar_matrix_product(alpha, matrix_variable):
    result = [[ alpha * element for element in t ] for t in matrix_variable]
    return result

#matrix_x = [[2,2], [2,3], [2,2]]
#matrix_y = [[2,5], [2,1]]
#matrix_z = [[2,4], [5,3]]
#matrix_w = [[2,5], [1,1], [2,2]]
#print(scalar_matrix_product(3, matrix_x))
#print(scalar_matrix_product(2, matrix_y))
#print(scalar_matrix_product(4, matrix_z))
#print(scalar_matrix_product(3, matrix_w))


#the number of A's column and B's row should be the same.
def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a[0]) == len(matrix_b)

#matrix_x= [[2, 5], [1, 1]]
#matrix_y = [[1, 1, 2], [2, 1, 1]]
#matrix_z = [[2, 4], [5, 3], [1, 3]]

#print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
#print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
#print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
#print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    #result = [ [ matrix_a_val * matrix_b_val for matrix_b_col in zip(*matrix_b) for matrix_b_val in matrix_b_col] \
    #         for matrix_a_row in matrix_a for matrix_a_val in matrix_a_row]
    result = [[ sum(a*b for a,b in zip(row_a, column_b)) \
                for column_b in zip(*matrix_b)] for row_a in matrix_a]
    return result

matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
#print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
#print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
#print(matrix_product(matrix_z, matrix_w)) # Expected value: False
