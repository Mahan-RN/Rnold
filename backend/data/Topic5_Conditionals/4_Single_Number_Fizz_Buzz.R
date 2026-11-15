#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 40
# title: Single Number FizzBuzz
# difficulty: 2

"--begin_description
You are given a number `num`.
Depending on the value of `num`, return one of the following:
- `FizzBuzz` if divisible by both 3 and 5
- `Fizz` if only divisible by 3
- `Buzz` if only divisible by 5
- `num` as string otherwise
--end_description"

# begin_starter_code
FizzBuzz <- function(num) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(FizzBuzz(15), "FizzBuzz")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(FizzBuzz(9), "Fizz")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(FizzBuzz(10), "Buzz")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(FizzBuzz(7), "7")
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(FizzBuzz(-15), "FizzBuzz")
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(FizzBuzz(0), "FizzBuzz")
#end_test_case