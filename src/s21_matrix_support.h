#ifndef S21_MATRIX_SUPPORT_H
#define S21_MATRIX_SUPPORT_H

#include "s21_var.h"

int is_null_matrix(matrix_t);
int is_some_null_matrix(matrix_t, matrix_t);
int is_different_matrix_size(matrix_t, matrix_t);
int is_MxK_KxN_matrix_size(matrix_t, matrix_t);
int is_quatro_size(matrix_t);
void print_matrix(matrix_t);
matrix_t copy_matrix(matrix_t);
matrix_t get_decreased_matrix(matrix_t, int, int);
double determinant(matrix_t);

#endif
