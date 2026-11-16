#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 30
# title: Is Filled
# difficulty: 1

"--begin_description
You are given a string `str`.
Return true if `str` is NOT empty and false otherwise.
--end_description"

# begin_starter_code
IsFilled <- function(str) {

    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(IsFilled(""), FALSE)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(IsFilled("abc"), TRUE)
#end_test_case