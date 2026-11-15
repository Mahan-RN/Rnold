#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 70
# title: Cube Root
# difficulty: 1

"--begin_description
You are given a number `num`.
Return its cube root.

You can assume that `num` is non-negative. This removes some complications that can arise from floating point arithmetic.

Hint: R does not provide a built-in function for cube root. How can you use exponentiation for this?
--end_description"

# begin_starter_code
CubeRoot <- function(num) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(0, CubeRoot(0))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(1, CubeRoot(1))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(2, CubeRoot(8))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(0.2, CubeRoot(0.008))
#end_test_case