#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 80
# title: Leap Year
# difficulty: 2

"--begin_description
You are given a year `year`.
A year is a leap year if it is divisible by `4`, except century years, which must also be divisible by `400`.
Determine if a given year is a leap year and return the result.

**Note:** century year is a year that is divisible by `100`. For exmple, 1900 or 2000.
--end_description"

# begin_starter_code
IsLeapYear <- function(year) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(IsLeapYear(2024), TRUE)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(IsLeapYear(1900), FALSE) 
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(IsLeapYear(2000), TRUE)
#end_test_case
