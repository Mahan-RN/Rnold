#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 40
# title: Valid Grade
# difficulty: 1

"--begin_description
A studnet grade `grade` is considered valid if it lies between 0 and 100 inclusive.
Determine if a given grade is valid and return the result.

You can assume that `grade` is always an integer.
--end_description"

# begin_starter_code
IsValidGrade <- function(grade) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(IsValidGrade(-1), FALSE)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(IsValidGrade(101), FALSE)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(IsValidGrade(0), TRUE)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(IsValidGrade(100), TRUE)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(IsValidGrade(50), TRUE)
#end_test_case