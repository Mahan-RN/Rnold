#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
install.packages("testthat")
# Load it
library(testthat)
# Note: all lines beween the two preabmle tags will be ignored by Rnold

#@ Problem
# topic_name:
# sort_order: 
# title:
# difficulty: [choose one of EASY/MEDIUM/HARD]

"--begin_description
Write your description here between the quotation marks.
This can be a multi-line description, with markdown syntax
--end_description"

# begin_starter_code
my_function <- function(arg1, arg2) {
    sum <- arg1 + arg2
    return(sum)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
expect_equal(4, my_function(2, 2))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
expect_equal(0, my_function(1, -1))
#end_test_case
