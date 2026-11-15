#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: String Manipulation
# sort_order: 20
# title: Sum of Lengths
# difficulty: 1

"--begin_description
You are given two strings `str1` and `str2`.
Return the sum of their lengths.

**Hint:** use the built-in `nchar()` function.
--end_description"

# begin_starter_code
SumOfLengths <- function(str1, str2) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(0, SumOfLengths("", ""))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(5, SumOfLengths("hello", ""))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(5, SumOfLengths("", "hello"))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(6, SumOfLengths("Cat", "Dog"))
#end_test_case