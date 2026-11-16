#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 40
# title: Divide Two Numbers
# difficulty: 1

"--begin_description
You are given two numbers `num1` and `num2`.
Divide `num1` by `num2` and return the result.

You can assume that `num2` is never zero.
--end_description"

# begin_starter_code
Divide <- function(num1, num2) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(Divide(0, 2), 0)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(Divide(2, 2), 1)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(Divide(4, 1), 4)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(Divide(1, 4), 0.25)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(Divide(144, 12), 12)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(Divide(12, -4), -3)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(Divide(-12, 4), -3)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(Divide(-12, -4), 3)
#end_test_case