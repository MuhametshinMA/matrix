#include "s21_matrix.h"

#include <math.h>
#include <stdlib.h>

#include "s21_matrix_support.h"

int s21_create_matrix(int row, int column, matrix_t* result) {
  int res = 0;
  if (row > 0 && column > 0 && result) {
    result->rows = row;
    result->columns = column;
    result->matrix = calloc(row, sizeof(double*));
    for (int i = 0; i < row; i++) {
      result->matrix[i] = calloc(column, sizeof(double));
    }
  } else {
    res = 1;
  }

  return res;
}

void s21_remove_matrix(matrix_t* A) {
  if (A->matrix) {
    for (int i = 0; i < A->rows; i++) {
      if (A->matrix[i]) {
        free(A->matrix[i]);
      }
    }

    if (A->matrix) {
      free(A->matrix);
    }
    A->columns = 0;
    A->rows = 0;
  }
}

int s21_eq_matrix(matrix_t* A, matrix_t* B) {
  int res = SUCCESS;

  if (is_some_null_matrix(*A, *B)) {
    res = FAILURE;
  }

  if (is_different_matrix_size(*A, *B)) {
    res = FAILURE;
  }
  if (res) {
    for (int i = 0; i < A->rows; i++) {
      for (int j = 0; j < A->columns; j++) {
        if (fabs(A->matrix[i][j] - B->matrix[i][j]) > EPS) {
          res = FAILURE;
        }
      }
    }
  }

  return res;
}

int s21_sum_matrix(matrix_t* A, matrix_t* B, matrix_t* result) {
  int res = 0;

  if (is_some_null_matrix(*A, *B)) {
    res = 1;
  }

  if (is_different_matrix_size(*A, *B)) {
    res = 2;
  }

  if (!res && !s21_create_matrix(A->rows, A->columns, result)) {
    for (int i = 0; i < A->rows; i++) {
      for (int j = 0; j < A->columns; j++) {
        result->matrix[i][j] = A->matrix[i][j] + B->matrix[i][j];
      }
    }
  }

  return res;
}

int s21_sub_matrix(matrix_t* A, matrix_t* B, matrix_t* result) {
  int res = 0;

  if (is_some_null_matrix(*A, *B)) {
    res = 1;
  }

  if (is_different_matrix_size(*A, *B)) {
    res = 2;
  }

  if (!res && !s21_create_matrix(A->rows, A->columns, result)) {
    for (int i = 0; i < A->rows; i++) {
      for (int j = 0; j < A->columns; j++) {
        result->matrix[i][j] = A->matrix[i][j] - B->matrix[i][j];
      }
    }
  }

  return res;
}

int s21_mult_number(matrix_t* A, double number, matrix_t* result) {
  int res = 0;

  if (is_null_matrix(*A)) {
    res = 1;
  }

  if (!res && !s21_create_matrix(A->rows, A->columns, result)) {
    for (int i = 0; i < A->rows; i++) {
      for (int j = 0; j < A->columns; j++) {
        result->matrix[i][j] = A->matrix[i][j] * number;
      }
    }
  }
  return res;
}

int s21_mult_matrix(matrix_t* A, matrix_t* B, matrix_t* result) {
  int res = 0;

  if (is_some_null_matrix(*A, *B)) {
    res = 1;
  }

  if (!res && !is_MxK_KxN_matrix_size(*A, *B)) {
    res = 2;
  }

  if (!res && !s21_create_matrix(A->rows, B->columns, result)) {
    for (int i = 0; i < result->rows; i++) {
      for (int j = 0; j < result->columns; j++) {
        for (int k = 0; k < A->columns; k++) {
          double a = A->matrix[i][k];
          double b = B->matrix[k][j];
          result->matrix[i][j] += a * b;
        }
      }
    }
  }

  return res;
}

int s21_transpose(matrix_t* A, matrix_t* result) {
  int res = 0;

  if (is_null_matrix(*A)) {
    res = 1;
  }

  if (!res && !s21_create_matrix(A->columns, A->rows, result)) {
    for (int i = 0; i < A->rows; i++) {
      for (int j = 0; j < A->columns; j++) {
        result->matrix[j][i] = A->matrix[i][j];
      }
    }
  }

  return res;
}

int s21_determinant(matrix_t* A, double* result) {
  int res = 0;

  if (is_null_matrix(*A)) {
    res = 1;
  }

  if (!is_quatro_size(*A)) {
    res = 2;
  }

  if (!res) {
    *result = determinant(*A);
  }

  return res;
}

int s21_calc_complements(matrix_t* A, matrix_t* result) {
  int res = 0;

  if (is_null_matrix(*A)) {
    res = 1;
  }

  if (!is_quatro_size(*A)) {
    res = 2;
  }

  if (!res) {
    matrix_t alg_add_m = {0};
    if (!s21_create_matrix(A->rows, A->rows, &alg_add_m)) {
      for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < A->rows; j++) {
          matrix_t dec_m = get_decreased_matrix(*A, i, j);
          alg_add_m.matrix[i][j] = pow(-1, i + j) * determinant(dec_m);
          s21_remove_matrix(&dec_m);
        }
      }
    }
    *result = alg_add_m;
  }

  return res;
}

int s21_inverse_matrix(matrix_t* A, matrix_t* result) {
  int res = 0;

  if (is_null_matrix(*A)) {
    res = 1;
  }

  if (!is_quatro_size(*A)) {
    res = 2;
  }

  if (!res) {
    if (A->rows == 1) {
      if (!s21_create_matrix(A->rows, A->rows, result)) {
        result->matrix[0][0] = 1 / A->matrix[0][0];
      }
    } else {
      matrix_t m_alg_adds = {0};
      double det = 0;
      if (!s21_calc_complements(A, &m_alg_adds) && !s21_determinant(A, &det)) {
        matrix_t m_alg_adds_det = {0};
        if (!s21_mult_number(&m_alg_adds, 1 / det, &m_alg_adds_det)) {
          if (!s21_transpose(&m_alg_adds_det, result)) {
          }
          s21_remove_matrix(&m_alg_adds_det);
        }
      }
      s21_remove_matrix(&m_alg_adds);
    }
  }

  return res;
}
