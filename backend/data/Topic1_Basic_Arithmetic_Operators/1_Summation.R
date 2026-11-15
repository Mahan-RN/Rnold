#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 10
# title: Sum of 3 Numbers
# difficulty: 1

"--begin_description
You are given three numbers `num1`, `num2`, and `num3`.
Return their sum.
--end_description"

# begin_starter_code
SumThree <- function(num1, num2, num3) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(sum(0, 0, 0), SumThree(0, 0, 0))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(sum(1, 2, 3), SumThree(1, 2, 3))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(sum(-1, -8, -1), SumThree(-1, -8, -1))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(sum(25, 25, -50), SumThree(25, 25, -50))
#end_test_case