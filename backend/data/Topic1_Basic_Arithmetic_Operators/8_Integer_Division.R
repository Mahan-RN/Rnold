#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 80
# title: Integer Division
# difficulty: 1

"--begin_description
You are given two numbers `num1` and `num2`.
Using integer division, divide `num1` by `num2` and return the result.

You can assume that `num2` is non-zero.

**What is integer division?** It's a division in which the fractional part of the result is discarded, rounding the result down towards negative infinity.

**Note:** in R, integer division and floor are the same.

--end_description"

# begin_starter_code
IntegerDivision <- function(num1, num2) {
    
    return(num1 %/% num2)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(0, IntegerDivision(0, 2))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(1, IntegerDivision(2, 2))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(4, IntegerDivision(4, 1))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(0, IntegerDivision(1, 4))
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(12, IntegerDivision(144, 12))
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(-3, IntegerDivision(12, -4))
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(-3, IntegerDivision(-12, 4))
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(3, IntegerDivision(-12, -4))
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(3, IntegerDivision(7, 2))
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(-4, IntegerDivision(-7, 2))
#end_test_case