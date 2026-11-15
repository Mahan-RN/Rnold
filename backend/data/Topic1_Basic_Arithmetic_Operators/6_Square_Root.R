#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 60
# title: Square Root
# difficulty: 1

"--begin_description
You are given a number `num`.
Return its square root.

You can assume that `num` is non-negative.
--end_description"

# begin_starter_code
SquareRoot <- function(num) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(0, SquareRoot(0))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(2, SquareRoot(4))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(13, SquareRoot(169))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(0.2, SquareRoot(0.04))
#end_test_case