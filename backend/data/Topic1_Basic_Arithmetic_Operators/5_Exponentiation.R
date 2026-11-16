#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 50
# title: Powers of Two
# difficulty: 1

"--begin_description
You are given a number `num`.
Raise `2` to the power of `num` and return the result.
--end_description"

# begin_starter_code
PowerOfTwo <- function(num) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(PowerOfTwo(0), 1)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(PowerOfTwo(3), 8)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(PowerOfTwo(10), 1024)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(PowerOfTwo(-1), 0.5)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(PowerOfTwo(-3), 0.125)
#end_test_case