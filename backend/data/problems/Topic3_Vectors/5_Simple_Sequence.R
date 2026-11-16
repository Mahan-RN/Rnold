#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Vectors
# sort_order: 50
# title: Simple Sequence
# difficulty: 1

"--begin_description
You are given three numbers: a starting value `start_index`, an ending value `stop_index`, and a step size `step_size`.

Generate and return a numeric vector starting at `start_index`, increasing by `step_size` until reaching or passing `stop_index`.

**Hint:** Use R's built-in `seq(from=x, to=y, by=z)` function.
--end_description"

# begin_starter_code
MakeSequence <- function(start_index, stop_index, step_size) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    MakeSequence(1, 5, 1),
    c(1, 2, 3, 4, 5)
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    MakeSequence(2, 10, 2),
    c(2, 4, 6, 8, 10)
)
#end_test_case