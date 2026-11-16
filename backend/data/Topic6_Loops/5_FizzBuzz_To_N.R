#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 50
# title: FizzBuzz Up To N
# difficulty: 3

"--begin_description
You are given a vector of positive integers `nums`.

Create and return a character vector by applying the following rules to each number:

- Return `'FizzBuzz'` if the number is divisible by both 3 and 5.
- Return `'Fizz'` if the number is divisible by 3 but not 5.
- Return `'Buzz'` if the number is divisible by 5 but not 3.
- Otherwise, return the number as a string.

The resulting vector should preserve the original order of the numbers.

If the input vector is empty, return an empty character vector.
--end_description"

# begin_starter_code
FuzzBuzzToN <- function(nums) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(FuzzBuzzToN(1), "1")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(FuzzBuzzToN(3), "Fizz")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(FuzzBuzzToN(5), "Buzz")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(FuzzBuzzToN(15), "FizzBuzz")
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(
    FuzzBuzzToN(c(1, 2, 3, 4, 5)),
    c("1", "2", "Fizz", "4", "Buzz")
)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(
    FuzzBuzzToN(c(3, 6, 9, 12)),
    c("Fizz", "Fizz", "Fizz", "Fizz")
)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(
    FuzzBuzzToN(c(5, 10, 20, 25)),
    c("Buzz", "Buzz", "Buzz", "Buzz")
)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(
    FuzzBuzzToN(c(15, 30, 45, 60)),
    c("FizzBuzz", "FizzBuzz", "FizzBuzz", "FizzBuzz")
)
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(
    FuzzBuzzToN(c(7, 9, 10, 11, 15, 17, 20)),
    c("7", "Fizz", "Buzz", "11", "FizzBuzz", "17", "Buzz")
)
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(FuzzBuzzToN(integer(0)), character(0))
#end_test_case