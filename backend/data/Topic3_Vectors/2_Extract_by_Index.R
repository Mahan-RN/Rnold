#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Vectors
# sort_order: 20
# title: Extract by Index
# difficulty: 1

"--begin_description
You are given a vector `vec` and an index `i`.
Return the i-th element of vec.

You can assume that `1 <= i <= length(vec)`.
--end_description"

# begin_starter_code
ExtractByIndex <- function(vec, i) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(ExtractByIndex(c(10, 20, 30, 40), 3), 30)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(ExtractByIndex(c("Cat", "Dog", "Duck", "Raven", "Fox"), 1), "Cat")
#end_test_case