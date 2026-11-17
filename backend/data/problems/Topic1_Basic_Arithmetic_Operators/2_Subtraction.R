#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 20
# title: Subtract Two Numbers
# difficulty: 1

"--begin_description
You are given two numbers `num1` and `num2`.
Subtract `num2` from `num1` and return the result.
--end_description"

# begin_starter_code
Subtract <- function(num1, num2) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(Subtract(0, 0), 0)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(Subtract(-1, -2), 1)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(Subtract(1, 2), -1)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(Subtract(-1, 2), -3)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(Subtract(1, -2), 3)
#end_test_case