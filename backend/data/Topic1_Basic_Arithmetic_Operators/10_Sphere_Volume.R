#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Basic Arithmetic Operations
# sort_order: 100
# title: Volume of a Sphere
# difficulty: 1

"--begin_description
You are given the diameter `diameter` of a sphere.
Return its volume using the formula `4/3 * pi * r^3` and return the result.

You can assume that `diameter` is a non-negative number.

**Hint:** R has a built-in constant `pi` for the pi number that you can use.
--end_description"

# begin_starter_code
SphereVolume <- function(diameter) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(0, SphereVolume(0))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(0.5235987756, SphereVolume(1))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(65.4498469498, SphereVolume(5))
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(0.0654498469, SphereVolume(0.5))
#end_test_case