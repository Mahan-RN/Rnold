#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 20
# title: Countdown
# difficulty: 2

"--begin_description
You are given a non-negative integer `n`.

Generate a countdown starting at `n` and ending at `0`.
Represent the countdown as a single string, with consecutive numbers separated by spaces.

After the countdown reaches zero, append `Liftoff!` to the string, separated by a space.

Return the resulting string.

For example, if `n` is 3, return `3 2 1 Liftoff!`.
--end_description"

# begin_starter_code
CountDown <- function(n) {

    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    CountDown(0),
    "Liftoff!"
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    CountDown(1),
    "1 Liftoff!"
)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(
    CountDown(3),
    "3 2 1 Liftoff!"
)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(
    CountDown(5),
    "5 4 3 2 1 Liftoff!"
)
#end_test_case