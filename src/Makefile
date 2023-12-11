CC=gcc
FLAGS=-Werror -Wall -Wextra -std=c11
FLAG_TEST=-lcheck
FLAG_GCOV=-fprofile-arcs -ftest-coverage
DFLAG=-Werror -Wall -Wextra -g -std=c11 -lm

SRC_FILES=s21_matrix.c s21_matrix_support.c
O_SRC_FILES=s21_matrix.o s21_matrix_support.o
ALL_FILES=s21_matrix.c s21_matrix.h s21_matrix_support.c s21_matrix_support.h s21_var.h

CHECK_FILES=test.check

TEST_FILES=test.c
O_TEST_FILES=test.o

OUT_FILE=s21_test

all: gcov_report


clean:
	rm -rf lcover_rep s21_test test.check *.o *.a *.out *.gcov *.gcno *.gcda *.gch *.info test.c

test: s21_matrix.a# py
	checkmk $(CHECK_FILES) > $(TEST_FILES)
	$(CC) $(FLAGS) -c $(TEST_FILES) $(FLAG_TEST)
	$(CC) $(FLAGS) -g $(O_TEST_FILES) s21_matrix.a -o $(OUT_FILE) $(FLAG_TEST)
	./$(OUT_FILE)

s21_matrix.a:
	$(CC) $(FLAGS) -c $(SRC_FILES)
	ar rc s21_matrix.a $(O_SRC_FILES)

gcov_report: test
	$(CC) $(FLAGS) $(FLAG_TEST) $(FLAG_GCOV) $(SRC_FILES) $(TEST_FILES)
	./a.out
	gcov $(SRC_FILES)


lcov_report:
	lcov --capture --directory . --output-file lcover.info
	genhtml lcover.info --output-directory lcover_rep
	open lcover_rep/index.html


d:
	$(CC) $(DFLAG) $(SRC_FILES) -o $(OUT_FILE)
	./$(OUT_FILE)

istyle:
	clang-format -i --style=google $(ALL_FILES)

nstyle:
	clang-format -n --style=google $(ALL_FILES)


val:
	valgrind --tool=memcheck --leak-check=full --track-origins=yes ./s21_test

py:
	# python3 test_py/test.py
	python3 test_py/test.py >> test.check
	# python3 -m venv venv //create environment
	# source venv/bin/activate //activate environment dir
	# eval "$(/opt/goinfre/littleca/homebrew/bin/brew shellenv)"