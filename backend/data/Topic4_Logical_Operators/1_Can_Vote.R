#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 10
# title: Can Vote
# difficulty: 1

"--begin_description
You are given the age of a person `age` and their citizenship status `is_citizen` as a boolean.
A person can only vote if they are 18 or older and have citizenship.
Evaluate if a person can vote and return the result.
--end_description"

# begin_starter_code
CanVote <- function(age, is_citizen) {

    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(FALSE, CanVote(17, FALSE))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(FALSE, CanVote(17, TRUE))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(FALSE, CanVote(18, FALSE))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(TRUE, CanVote(18, TRUE))
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(TRUE, CanVote(50, TRUE))
#end_test_case
