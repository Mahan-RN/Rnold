#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 10
# title: Number Sign
# difficulty: 2

"--begin_description
You are given a number `num`.
Return a string describing the number, using the followig format:
- Negative Numbers: `n is negative`
- Positive Numbers: `n is positive`
- Zero: `n is zero`
--end_description"

# begin_starter_code
SignLabel <- function(num) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(SignLabel(-1), "-1 is negative")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(SignLabel(0), "0 is zero")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(SignLabel(1), "1 is positive")
#end_test_case
