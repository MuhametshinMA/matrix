import random
import numpy as np


class Matrix:
    @staticmethod
    def create_shape_rand_matrix(row, col):
        matrix = np.zeros((row, col))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                matrix[i][j] = round(random.uniform(0, 10), 7)

        return matrix

    @staticmethod
    def create_rand_matrix():
        random.seed()
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        matrix = np.zeros((row, col))

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                matrix[i][j] = round(random.uniform(0, 10), 7)

        return matrix

    @staticmethod
    def print_fill_matrix(name, m):
        if (m.shape[0] and m.shape[1]):
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    print('    '+name+'.matrix[' + str(i) +
                          '][' + str(j) + ']=', end='')
                    print(round(m[i][j], 7), end='; ')
                print('')

    @staticmethod
    def print_inverse_matrix_test(index):
        print("#test inverse_matrix_test_{0}" .format(index))
        row = random.randrange(0, 7)
        num = random.randint(0, 1)
        col = row + num
        m = Matrix.create_shape_rand_matrix(row, col)
        print("  matrix_t m1 = {0};")
        print("  matrix_t s21 = {0};")
        print("  s21_create_matrix("+str(row)+", "+str(col)+", &m1);")
        if (row and col and row == col):
            m_inv = np.linalg.inv(m)
            # print("\033[32m")
            print("  matrix_t ori = {0};")
            print("  s21_create_matrix("+str(row)+", "+str(col)+", &ori);")
            Matrix.print_fill_matrix("ori", m_inv)
            Matrix.print_fill_matrix("m1", m)
            print("  int code = s21_inverse_matrix(&m1, &s21);")
            print("  ck_assert_int_eq(0, code);")
            print("  s21_remove_matrix(&ori);")
            # print("\033[0m")
        elif (row and col):
            # print("\033[31m")
            # print("not null")
            print("  int code = s21_inverse_matrix(&m1, &s21);")
            print("  ck_assert_int_eq(2, code);")
            # print("\033[0m")
        else:
            # print("\033[3;31m")
            # print("null")
            print("  int code = s21_inverse_matrix(&m1, &s21);")
            print("  ck_assert_int_eq(1, code);")
            # print("\033[0m")
        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&s21);")

    @staticmethod
    def print_alg_add_matrix_test(index):
        print("#test alg_add_matrix_test_{0}" .format(index))
        row = random.randrange(0, 7)
        num = random.randint(0, 1)
        col = row + num
        m = Matrix.create_shape_rand_matrix(row, col)
        print("  matrix_t m1 = {0};")
        print("  matrix_t s21 = {0};")
        print("  s21_create_matrix("+str(row)+", "+str(col)+", &m1);")
        if (row and col and row == col):
            det = np.linalg.det(m)
            m_inv = np.linalg.inv(m)
            m_inv_trans = m_inv.transpose()
            m_alg_add = m_inv_trans * det
            # print("\033[32m")
            print("  matrix_t ori = {0};")
            print("  s21_create_matrix("+str(row)+", "+str(col)+", &ori);")
            Matrix.print_fill_matrix("ori", m_alg_add)
            Matrix.print_fill_matrix("m1", m)
            print("  int code = s21_calc_complements(&m1, &s21);")
            print("  ck_assert_int_eq(0, code);")
            print("  s21_remove_matrix(&ori);")
            # print("\033[0m")
        elif (row and col):
            # print("\033[31m")
            # print("not null")
            print("  int code = s21_calc_complements(&m1, &s21);")
            print("  ck_assert_int_eq(2, code);")
            # print("\033[0m")
        else:
            # print("\033[3;31m")
            # print("null")
            print("  int code = s21_calc_complements(&m1, &s21);")
            print("  ck_assert_int_eq(1, code);")
            # print("\033[0m")
        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&s21);")

                
    @staticmethod
    def print_det_test(index):
        print("#test det_test_{0}" .format(index))
        row = random.randrange(0, 7)
        num = random.randint(0, 1)
        col = row + num
        m = Matrix.create_shape_rand_matrix(row, col)
        print("  matrix_t m1 = {0};")
        print("  double s21 = 0;")
        print("  s21_create_matrix("+str(row)+", "+str(col)+", &m1);")
        if (row and col and row == col):
            # print("\033[32m")
            Matrix.print_fill_matrix("m1", m)
            print("  int code = s21_determinant(&m1, &s21);")
            print("  double ori = {};" .format(np.linalg.det(m)))
            print("  ck_assert_int_eq(0, code);")
            print("  ck_assert_double_le(fabs(ori - s21), EPS);")
            # print("\033[0m")
        elif (row and col):
            # print("\033[31m")
            # print("not null")
            print("  int code = s21_determinant(&m1, &s21);")
            print("  ck_assert_int_eq(2, code);")
            # print("\033[0m")
        else:
            # print("\033[3;31m")
            # print("null")
            print("  int code = s21_determinant(&m1, &s21);")
            print("  ck_assert_int_eq(1, code);")
            # print("\033[0m")
        print("  s21_remove_matrix(&m1);")

    @staticmethod
    def print_trans_test(index):
        print("#test trans_test_{0}" .format(index))
        row = random.randrange(0, 7)
        col = random.randrange(0, 7)
        m = Matrix.create_shape_rand_matrix(row, col)
        print("  matrix_t m1 = {0};")
        print("  matrix_t s21 = {0};")
        print("  s21_create_matrix("+str(row)+", "+str(col)+", &m1);")
        if (row and col):
            Matrix.print_fill_matrix("m1", m)
            m_trans = m.transpose()
            print("  matrix_t ori = {0};")
            print("  s21_create_matrix(" +
                  str(m_trans.shape[0])+", "+str(m_trans.shape[1])+", &ori);")
            Matrix.print_fill_matrix("ori", m_trans)
            print("  int code = s21_transpose(&m1, &s21);")
            print("  ck_assert_int_eq(0, code);")
            print("  ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
            print("  s21_remove_matrix(&ori);")
        else:
            print("  int code = s21_transpose(&m1, &s21);")
            print("  ck_assert_int_eq(1, code);")
        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&s21);")

    @staticmethod
    def print_mul_test(index):
        print("#test mul_test_{0}" .format(index))
        row1 = random.randrange(0, 7)
        col1 = random.randrange(0, 7)
        num = random.randint(0, 1)
        row2 = col1 + num
        col2 = random.randrange(0, 7)
        m1 = Matrix.create_shape_rand_matrix(row1, col1)
        m2 = Matrix.create_shape_rand_matrix(row2, col2)
        incorrect = 0
        try:
            total = m1.dot(m2)
        except ValueError:
            incorrect = 1
        # print("{")
        print("  matrix_t m1 = {0};")
        print("  matrix_t m2 = {0};")
        print("  matrix_t ori = {0};")
        print("  matrix_t s21 = {0};")
        print("  s21_create_matrix("+str(row1)+", "+str(col1)+", &m1);")
        print("  s21_create_matrix("+str(row2)+", "+str(col2)+", &m2);")
        if (not incorrect and row1 and col1 and row2 and col2):
            # print("\033[32m")
            print("  s21_create_matrix("+str(row1)+", "+str(col2)+", &ori);")
            Matrix.print_fill_matrix("ori", total)
            Matrix.print_fill_matrix("m1", m1)
            Matrix.print_fill_matrix("m2", m2)
            print("  int code = s21_mult_matrix(&m1, &m2, &s21);")
            print("  ck_assert_int_eq(0, code);")
            print("  ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
            # print("\033[0m")
        elif (not (row1 and col1 and row2 and col2)):
            # print("\033[31m")
            print("  int code = s21_mult_matrix(&m1, &m2, &s21);")
            print("  ck_assert_int_eq(1, code);")
            # print("\033[0m")
        elif incorrect:
            # print("\033[3;31m")
            print("  int code = s21_mult_matrix(&m1, &m2, &s21);")
            print("  ck_assert_int_eq(2, code);")
            # print("\033[0m")
        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&m2);")
        print("  s21_remove_matrix(&ori);")
        print("  s21_remove_matrix(&s21);")
        # print("}")

    @staticmethod
    def print_mul_num_test(index):

        print("#test mul_num_test_{0}" .format(index))
        m1 = Matrix.create_rand_matrix()
        num = random.random() * random.randrange(10)
        msum = m1 * num
        print("{")
        print("  double num = " + str(num) + ";")
        print("  matrix_t m1 = {0};")
        print("  matrix_t ori = {0};")
        print("  int row = "+str(m1.shape[0])+";")
        print("  int col = "+str(m1.shape[1])+";")
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &m1);")
        Matrix.print_fill_matrix("m1", m1)

        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &ori);")
        Matrix.print_fill_matrix("ori", msum)
        print("  matrix_t s21 = {0};")
        print("  if (row && col) {")
        print("    ck_assert_int_eq(0, s21_mult_number(&m1, num, &s21));")
        print("    ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
        print("    s21_remove_matrix(&m1);")
        print("    s21_remove_matrix(&ori);")
        print("    s21_remove_matrix(&s21);")
        print("  } else {")
        print("    ck_assert_int_eq(1, s21_mult_number(&m1, num, &s21));")
        print("    ck_assert_int_eq(0, s21_eq_matrix(&s21, &ori));")
        print("  }")
        print("}")

    @staticmethod
    def print_sub_test(index):
        # sub 0, 1
        print("#test sub_test_{0}" .format(index))
        m1 = Matrix.create_rand_matrix()
        m2 = Matrix.create_shape_rand_matrix(m1.shape[0], m1.shape[1])
        msub = m1 - m2
        print("{")
        print("  matrix_t m1 = {0};")
        print("  matrix_t m2 = {0};")
        print("  matrix_t ori = {0};")
        print("  int row = "+str(m1.shape[0])+";")
        print("  int col = "+str(m1.shape[1])+";")
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &m1);")
        Matrix.print_fill_matrix("m1", m1)
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &m2);")
        Matrix.print_fill_matrix("m2", m2)
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &ori);")
        Matrix.print_fill_matrix("ori", msub)
        print("  matrix_t s21 = {0};")
        print("  if (row && col) {")
        print("    ck_assert_int_eq(0, s21_sub_matrix(&m1, &m2, &s21));")
        print("    ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
        print("    s21_remove_matrix(&m1);")
        print("    s21_remove_matrix(&m2);")
        print("    s21_remove_matrix(&ori);")
        print("    s21_remove_matrix(&s21);")
        print("  } else {")
        print("    ck_assert_int_eq(1, s21_sub_matrix(&m1, &m2, &s21));")
        print("    ck_assert_int_eq(0, s21_eq_matrix(&s21, &ori));")
        print("  }")
        print("}")
        # sub 0, 1

        # sub 2
        row1 = random.randrange(2, 7)
        col1 = random.randrange(2, 7)
        m1 = Matrix.create_shape_rand_matrix(row1, col1)
        row2 = row1 + random.randint(0, 1)
        col2 = col1 - random.randint(0, 1)
        m2 = Matrix.create_shape_rand_matrix(row2, col2)
        print("{")
        print("  matrix_t m1 = {0};")
        print("  matrix_t m2 = {0};")
        print("  matrix_t ori = {0};")
        print("  int row1 = "+str(m1.shape[0])+";")
        print("  int col1 = "+str(m1.shape[1])+";")
        print("  int row2 = "+str(m2.shape[0])+";")
        print("  int col2 = "+str(m2.shape[1])+";")
        print("  s21_create_matrix(row1, col1, &m1);")
        print("  s21_create_matrix(row2, col2, &m2);")
        print("  s21_create_matrix(row1, col1, &ori);")
        print("  matrix_t s21 = {0};")
        print("  if ((row1 != row2) || (col1 != col2)) {")
        if ((row1 != row2) or (col1 != col2)):
            print("    ck_assert_int_eq(2, s21_sub_matrix(&m1, &m2, &s21));")
            print("    ck_assert_int_eq(0, s21_eq_matrix(&s21, &ori));")
            print("  }")
        else:
            print("  } else {")
            msub = m1 - m2
            Matrix.print_fill_matrix("m1", m1)
            Matrix.print_fill_matrix("m2", m2)
            Matrix.print_fill_matrix("ori", msub)
            print("    ck_assert_int_eq(0, s21_sub_matrix(&m1, &m2, &s21));")
            print("    ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
            print("  }")

        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&m2);")
        print("  s21_remove_matrix(&ori);")
        print("  s21_remove_matrix(&s21);")
        print("}")
        # sub 2

    @staticmethod
    def print_sum_test(index):
        # sum 0, 1
        print("#test sum_test_{0}" .format(index))
        m1 = Matrix.create_rand_matrix()
        m2 = Matrix.create_shape_rand_matrix(m1.shape[0], m1.shape[1])
        msum = m1 + m2
        print("{")
        print("  matrix_t m1 = {0};")
        print("  matrix_t m2 = {0};")
        print("  matrix_t ori = {0};")
        print("  int row = "+str(m1.shape[0])+";")
        print("  int col = "+str(m1.shape[1])+";")
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &m1);")
        Matrix.print_fill_matrix("m1", m1)
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &m2);")
        Matrix.print_fill_matrix("m2", m2)
        print("  s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &ori);")
        Matrix.print_fill_matrix("ori", msum)
        print("  matrix_t s21 = {0};")
        print("  if (row && col) {")
        print("    ck_assert_int_eq(0, s21_sum_matrix(&m1, &m2, &s21));")
        print("    ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
        print("  } else {")
        print("    ck_assert_int_eq(1, s21_sum_matrix(&m1, &m2, &s21));")
        print("    ck_assert_int_eq(0, s21_eq_matrix(&s21, &ori));")
        print("  }")
        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&m2);")
        print("  s21_remove_matrix(&ori);")
        print("  s21_remove_matrix(&s21);")
        print("}")
        # sum 0, 1

        # sum 2
        row1 = random.randrange(2, 7)
        col1 = random.randrange(2, 7)
        m1 = Matrix.create_shape_rand_matrix(row1, col1)
        row2 = row1 + random.randint(0, 1)
        col2 = col1 - random.randint(0, 1)
        m2 = Matrix.create_shape_rand_matrix(row2, col2)
        print("{")
        print("  matrix_t m1 = {0};")
        print("  matrix_t m2 = {0};")
        print("  matrix_t ori = {0};")
        print("  int row1 = "+str(m1.shape[0])+";")
        print("  int col1 = "+str(m1.shape[1])+";")
        print("  int row2 = "+str(m2.shape[0])+";")
        print("  int col2 = "+str(m2.shape[1])+";")
        print("  s21_create_matrix(row1, col1, &m1);")
        print("  s21_create_matrix(row2, col2, &m2);")
        print("  s21_create_matrix(row1, col1, &ori);")
        print("  matrix_t s21 = {0};")
        print("  if ((row1 != row2) || (col1 != col2)) {")
        if ((row1 != row2) or (col1 != col2)):
            print("    ck_assert_int_eq(2, s21_sum_matrix(&m1, &m2, &s21));")
            print("    ck_assert_int_eq(0, s21_eq_matrix(&s21, &ori));")
            print("  }")
        else:
            print("  } else {")
            msum = m1 + m2
            Matrix.print_fill_matrix("m1", m1)
            Matrix.print_fill_matrix("m2", m2)
            Matrix.print_fill_matrix("ori", msum)
            print("    ck_assert_int_eq(0, s21_sum_matrix(&m1, &m2, &s21));")
            print("    ck_assert_int_eq(1, s21_eq_matrix(&s21, &ori));")
            print("  }")

        print("  s21_remove_matrix(&m1);")
        print("  s21_remove_matrix(&m2);")
        print("  s21_remove_matrix(&ori);")
        print("  s21_remove_matrix(&s21);")
        print("}")
        # sum 2

    @staticmethod
    def print_equal_test(index):
        print("#test equal_test_{0}" .format(index))
        m1 = Matrix.create_rand_matrix()
        m2 = m1.copy()
        rand_row = 0
        rand_col = 0
        num = random.randint(0, 1)
        print("  matrix_t m1 = {0};")
        print("  if (!s21_create_matrix(" +
              str(m1.shape[0])+", "+str(m1.shape[1])+", &m1)) {")
        if (m1.shape[0] and m1.shape[1]):
            rand_row = random.randrange(m1.shape[0])
            rand_col = random.randrange(m1.shape[1])
            for i in range(m1.shape[0]):
                for j in range(m1.shape[1]):
                    print('    m1.matrix[' + str(i) +
                          '][' + str(j) + ']=', end='')
                    print(m1[i][j], end='; ')
                print('')
            print("    matrix_t m2 = copy_matrix(m1);")
            m1[rand_row][rand_col] *= num
            print("    m1.matrix["+str(rand_row)+"][" +
                  str(rand_col)+"] *= "+str(num)+";")
            print("    int eq = s21_eq_matrix(&m1, &m2);")
            print("    ck_assert_int_eq("+str(int(np.array_equal(m1, m2)))+", eq);")
            print("    s21_remove_matrix(&m1);")
            print("    s21_remove_matrix(&m2);")
            print("  }")
        else:
            print("  } else {")
            print("    matrix_t m2 = copy_matrix(m1);")
            print("    ck_assert_int_eq(0, s21_eq_matrix(&m1, &m2));")
            print("  }")

    @staticmethod
    def print_no_fork_test():
        print("#main-pre")
        print("  srunner_set_fork_status(sr, CK_NOFORK);")

    @staticmethod
    def print_header_test():
        print("#include <stdlib.h>")
        print("#include <stdio.h>")
        print("#include \"s21_matrix.h\"")
        print("#include \"s21_matrix_support.h\"")
