#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 70
# title: Digit Sum
# difficulty: 3

"--begin_description
You are given a non-negative integer `n`.

Calculate and return the sum of all its digits.

For example, if `n = 493`, return `16` because `4 + 9 + 3 = 16`.

If `n` is `0`, return `0`.
--end_description"

# begin_starter_code
DigitSum <- function(n) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(DigitSum(0), 0)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(DigitSum(5), 5)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(DigitSum(12), 3)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(DigitSum(493), 16)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(DigitSum(100), 1)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(DigitSum(1010), 2)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(DigitSum(999), 27)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(DigitSum(12345), 15)
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(DigitSum(1000000), 1)
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(DigitSum(987654321), 45)
#end_test_case