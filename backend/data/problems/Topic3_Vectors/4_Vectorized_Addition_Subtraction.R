#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Vectors
# sort_order: 40
# title: Vectorized Addition and Subtraction
# difficulty: 1

"--begin_description
You are given two vectors of numbers `nums1` and `nums2` and a constant `x`.
Add `nums1` and `nums2`, then multiply the result by `2`. Finally, subtract `x` from the resulting vector and return it.
--end_description"

# begin_starter_code
VectorizedMess <- function(nums1, nums2, x) {

    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    VectorizedMess(c(1, 2, 3), c(4, 5, 6), 2),
    c(8, 12, 16)
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    VectorizedMess(c(-2, 0, 5), c(3, -4, 1), 3),
    c(-1, -11, 9)
)
#end_test_case