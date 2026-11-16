#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 50
# title: Filter Even Numbers
# difficulty: 1

"--begin_description
You are given a vector of numbers `nums`.
Filter nums to only keep even numbers and return the result.
--end_description"

# begin_starter_code
FilterEvens <- function(nums) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(FilterEvens(c()), 
                       c())
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(FilterEvens(1:10), 
                       c(2, 4, 6, 8, 10))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(FilterEvens(c(2, 4, 6)), 
                       c(2, 4, 6))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(FilterEvens(c(101, 103, 105)), 
                       numeric(0))
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(FilterEvens(c(1001, 1006)), 
                       c(1006))
#end_test_case
