#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 90
# title: Modulus (Remainder)
# difficulty: 1

"--begin_description
You are given two numbers `num1` and `num2`.
Divide `num1` by `num2` and return the remainder.

You can assume that `num2` is non-zero.

**Hint:** use modulo operator

**What is modulo?** modulo operation calculates the remainder left over after dividing one integer by another. 
--end_description"

# begin_starter_code
Modulo <- function(num1, num2) {
    
    return(num1 %% num2)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(0, Modulo(0, 5))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(0, Modulo(2, 2))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(0, Modulo(1024, 2))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(-1, Modulo(5, -2))
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(-1, Modulo(-5, -2))
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(1, Modulo(-5, 2))
#end_test_case