#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 80
# title: Guessing Game
# difficulty: 3

"--begin_description
You are given a numeric vector `guesses` containing guesses in the order they were made, and a number `secret`.

Process the guesses in order until one matches `secret`.

- If a guess matches, return a message in the format `'Found 7 on attempt 3'`, replacing `7` with the secret number and `3` with the position of the matching guess.
- If none of the guesses match, return a message in the format `'Not found after 3 guesses'`, replacing `3` with the total number of guesses.
--end_description"

# begin_starter_code
GuessingGame <- function(guesses, secret) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(7, 3, 5), 7),
    "Found 7 on attempt 1"
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(1, 2, 7), 7),
    "Found 7 on attempt 3"
)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(4, 7, 9, 7), 7),
    "Found 7 on attempt 2"
)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(1, 2, 3, 4, 5), 9),
    "Not found after 5 guesses"
)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(10), 5),
    "Not found after 1 guesses"
)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(5), 5),
    "Found 5 on attempt 1"
)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(2, 4, 6, 8, 10), 10),
    "Found 10 on attempt 5"
)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(7, 3, 7, 9), 7),
    "Found 7 on attempt 1"
)
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(
    GuessingGame(numeric(0), 7),
    "Not found after 0 guesses"
)
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(
    GuessingGame(c(1, 2, 3, 4, 5, 6), 6),
    "Found 6 on attempt 6"
)
#end_test_case