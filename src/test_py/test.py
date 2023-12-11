import numpy as np
# import random
from Matrix import Matrix

# matrix1 = Matrix.create_rand_matrix()
# matrix2 = Matrix.create_shape_rand_matrix(matrix1.shape[0], matrix1.shape[1])

# try:
#     total = matrix1 + matrix2
# except ValueError:
#     print("incorrect matrix")

Matrix.print_header_test()
for i in range(20):
    Matrix.print_equal_test(i)
for i in range(20):
    Matrix.print_sum_test(i)
for i in range(20):
    Matrix.print_sub_test(i)
for i in range(20):
    Matrix.print_mul_test(i)
for i in range(20):
    Matrix.print_trans_test(i)
for i in range(20):
    Matrix.print_det_test(i)
for i in range(20):
    Matrix.print_alg_add_matrix_test(i)
for i in range(20):
    Matrix.print_inverse_matrix_test(i)
Matrix.print_no_fork_test()
