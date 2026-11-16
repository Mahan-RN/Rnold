#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 30
# title: Yes or No Command
# difficulty: 2

"--begin_description
You are given a string `command` representing a user's response.

Return the following string depending on the value of `command`:
- `Confirmed` if `command` is `yes` or `y`.
- `Cancelled` if `command` is `no` or `n`.
- `Unknown command: <command>` for any other input, replacing `<command>` with the provided value.

--end_description"

# begin_starter_code
Respond <- function(command) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(Respond("yes"), "Confirmed")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(Respond("y"), "Confirmed")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(Respond("no"), "Cancelled")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(Respond("n"), "Cancelled")
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(Respond("maybe"), "Unknown command: maybe")
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(Respond(""), "Unknown command: ")
#end_test_case
