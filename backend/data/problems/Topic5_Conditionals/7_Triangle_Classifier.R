#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 70
# title: Triangle Classifier
# difficulty: 2

"--begin_description
You are given three positive side lengths: `a`, `b`, and `c`.

Classify the triangle based on its side lengths and return one of the following strings:
- `Not a triangle` if the sum of any two side lengths is less than or equal to the third.
- `Equilateral` if all three side lengths are equal.
- `Isosceles` if exactly two side lengths are equal.
- `Scalene` if all three side lengths are different.

--end_description"

# begin_starter_code
TriangleClassifier <- function(a, b, c) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    TriangleClassifier(5, 5, 5),
    "Equilateral"
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    TriangleClassifier(5, 5, 8),
    "Isosceles"
)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(
    TriangleClassifier(3, 4, 5),
    "Scalene"
)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(
    TriangleClassifier(1, 2, 3),
    "Not a triangle"
)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(
    TriangleClassifier(1, 2, 4),
    "Not a triangle"
)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(
    TriangleClassifier(3, 5, 5),
    "Isosceles"
)
#end_test_case