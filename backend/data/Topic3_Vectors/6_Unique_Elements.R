#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Vectors
# sort_order: 60
# title: Unique Elements
# difficulty: 1

"--begin_description
You are given a vector of elements `vec`.
Remove all duplicate values while preserving the original order of the elements.
Return the resulting vector.
--end_description"

# begin_starter_code
UniqueElements <- function(vec) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    UniqueElements(c(1, 2, 2, 3, 3, 3)),
    c(1, 2, 3)
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    UniqueElements(c("apple", "banana", "apple", "orange", "banana")),
    c("apple", "banana", "orange")
)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(
    UniqueElements(c(5, 5, 5, 5)),
    5
)
#end_test_case