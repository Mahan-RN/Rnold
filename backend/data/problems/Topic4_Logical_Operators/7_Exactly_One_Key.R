#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 70
# title: Exactly One Switch
# difficulty: 2

"--begin_description
You are given two switches `a` and `b` that are booleans. A switch is on if it is true.
A door opens when exactly one of the two switches is on.
Evaluate if a given combination of switches opens the door and return the result.

**Hint:** lookup XOR operator
--end_description"

# begin_starter_code
OpenDoor <- function(a , b) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(OpenDoor(FALSE, FALSE), 
                       FALSE)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(OpenDoor(TRUE, TRUE), 
                       FALSE)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(OpenDoor(TRUE, FALSE), 
                       TRUE)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(OpenDoor(FALSE, TRUE), 
                       TRUE)
#end_test_case
