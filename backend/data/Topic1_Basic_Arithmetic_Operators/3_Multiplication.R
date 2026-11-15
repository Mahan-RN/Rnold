#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 30
# title: Multiply Two Numbers
# difficulty: 1

"--begin_description
You are given two numbers `num1` and `num2`.
Return their product.
--end_description"

# begin_starter_code
Multiply <- function(num1, num2) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(prod(0, 0), Multiply(0, 0))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(prod(0, 5), Multiply(0, 5))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(prod(5, 0), Multiply(5, 0))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(prod(5, 5), Multiply(5, 5))
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(prod(-5, 5), Multiply(-5, 5))
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(prod(5, -5), Multiply(5, -5))
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(prod(-5, -5), Multiply(-5, -5))
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(prod(6, 15), Multiply(6, 15))
#end_test_case