#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 40
# title: Greet Everyone
# difficulty: 2

"--begin_description
You are given a character vector `names` containing people's names.

Create and return a character vector of greetings, where each greeting follows the format `'Hello, NAME!'`. Replace `NAME` with the corresponding name converted to uppercase.

The greetings should appear in the same order as the input names.

If the input vector is empty, return an empty character vector.
--end_description"

# begin_starter_code
GreetAll <- function(names) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(GreetAll("Sara"), "Hello, SARA!")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(GreetAll("john"), "Hello, JOHN!")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(GreetAll("ALICE"), "Hello, ALICE!")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(GreetAll("mArY"), "Hello, MARY!")
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(
    GreetAll(c("Sara", "John")),
    c("Hello, SARA!", "Hello, JOHN!")
)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(
    GreetAll(c("alice", "BOB", "Charlie")),
    c("Hello, ALICE!", "Hello, BOB!", "Hello, CHARLIE!")
)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(
    GreetAll(c("anna lee", "john smith")),
    c("Hello, ANNA LEE!", "Hello, JOHN SMITH!")
)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(
    GreetAll(c("A", "B", "C")),
    c("Hello, A!", "Hello, B!", "Hello, C!")
)
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(GreetAll(character(0)), character(0))
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(
    GreetAll(c("sara", "sara", "john")),
    c("Hello, SARA!", "Hello, SARA!", "Hello, JOHN!")
)
#end_test_case