#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 10
# title: Sum to N
# difficulty: 2

"--begin_description
You are given a positive integer `n`.

Calculate and return the sum of all integers from 1 through `n`, inclusive.

Assume `n` is an integer such that `n >= 1`.
--end_description"

# begin_starter_code
SumToN <- function(n) {
   
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(SumToN(1), 1)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(SumToN(2), 3)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(SumToN(5), 15)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(SumToN(10), 55)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(SumToN(100), 5050)
#end_test_case