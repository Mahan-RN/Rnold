#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Vectors
# sort_order: 30
# title: Replace by Index
# difficulty: 1

"--begin_description
You are given a vector `vec`, an index `i`, and an object `new_element`
Replace the `i`-th element of `vec` with `new_element` and return the resulting vector. 

You can assume that `1 <= i <= length(vec)`.
You can assume that new_element has the same type as the other elements in `vec`
--end_description"

# begin_starter_code
ReplaceByIndex <- function(vec, i, new_element) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(ReplaceByIndex(c("Canada", "", "Mexico"), 2, "USA"), c("Canada", "USA", "Mexico"))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(ReplaceByIndex(c(100, 200, 300, 400, 5), 5, 500), c(100, 200, 300, 400, 500))
#end_test_case