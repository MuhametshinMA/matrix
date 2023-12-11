#include "s21_matrix_support.h"

#include <math.h>
#include <stdio.h>

#include "s21_matrix.h"

int is_null_matrix(matrix_t A) { return !(A.rows && A.columns); }

int is_some_null_matrix(matrix_t A, matrix_t B) {
  return is_null_matrix(A) || is_null_matrix(B);
}

matrix_t copy_matrix(matrix_t A) {
  matrix_t res = {0};
  if (!s21_create_matrix(A.rows, A.columns, &res)) {
    for (int i = 0; i < A.rows; i++) {
      for (int j = 0; j < A.columns; j++) {
        res.matrix[i][j] = A.matrix[i][j];
      }
    }
  }
  return res;
}

int is_different_matrix_size(matrix_t A, matrix_t B) {
  return (A.rows != B.rows) || (A.columns != B.columns);
}

int is_MxK_KxN_matrix_size(matrix_t A, matrix_t B) {
  return A.columns == B.rows;
}

int is_quatro_size(matrix_t A) { return A.rows == A.columns; }

matrix_t get_decreased_matrix(matrix_t A, int row, int col) {
  matrix_t dec_m = {0};
  if (!s21_create_matrix(A.rows - 1, A.columns - 1, &dec_m)) {
    for (int i = 0, ii = 0; i < A.rows; i++) {
      if (row != i) {
        for (int j = 0, jj = 0; j < A.rows; j++) {
          if (col != j) {
            dec_m.matrix[ii][jj] = A.matrix[i][j];
            jj++;
          }
        }
        ii++;
      }
    }
  }
  return dec_m;
}

double determinant(matrix_t A) {
  double det = 0;
  if (A.rows == 1) {
    det = A.matrix[0][0];
  }
  if (A.rows == 2) {
    det = A.matrix[0][0] * A.matrix[1][1] - A.matrix[0][1] * A.matrix[1][0];
  }
  if (A.rows == 3) {
    det = A.matrix[0][0] * A.matrix[1][1] * A.matrix[2][2] +
          A.matrix[0][1] * A.matrix[1][2] * A.matrix[2][0] +
          A.matrix[0][2] * A.matrix[1][0] * A.matrix[2][1] -
          A.matrix[0][0] * A.matrix[1][2] * A.matrix[2][1] -
          A.matrix[0][1] * A.matrix[1][0] * A.matrix[2][2] -
          A.matrix[0][2] * A.matrix[1][1] * A.matrix[2][0];
  }
  if (A.rows > 3) {
    for (int i = 0; i < A.rows; i++) {
      matrix_t dec_m = get_decreased_matrix(A, 0, i);
      det += pow(-1, i) * A.matrix[0][i] * determinant(dec_m);
      s21_remove_matrix(&dec_m);
    }
  }

  return det;
}
