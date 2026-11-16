#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 60
# title: Years to Double
# difficulty: 3

"--begin_description
You are given the starting balance of a bank account `balance` and its annual interest rate `rate`.

Assuming interest is compounded once per year, calculate how many whole years it takes for the balance to reach or exceed twice its starting value.

Return the smallest number of whole years needed to reach the target.

If `rate` is zero or negative, return `'Never'`.

Assume:
- `balance` is non-negative.
- `rate` is a percentage (e.g., `5` represents 5% annual interest).
--end_description"

# begin_starter_code
YearsToDouble <- function(balance, rate) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 100), 1)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 50), 2)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 25), 4)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 10), 8)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 5), 15)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 1), 70)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(YearsToDouble(100, 0), "Never")
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(YearsToDouble(100, -5), "Never")
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(YearsToDouble(0, 10), 0)
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(YearsToDouble(250, 20), 4)
#end_test_case