#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Loops
# sort_order: 30
# title: Count Passing Grades
# difficulty: 2

"--begin_description
You are given a numeric vector `grades` representing student grades.

Count how many grades are greater than or equal to 50 (passing grades) and return the count.

If the vector is empty, return `0`.

Assume that every grade is a number between 0 and 100, inclusive.
--end_description"

# begin_starter_code
CountPassingGrades <- function(grades) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(60)), 1)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(40)), 0)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(50)), 1)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(49, 50, 51)), 2)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(0, 25, 49, 50)), 1)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(50, 60, 70, 80, 90, 100)), 6)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(10, 20, 30, 40)), 0)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(45, 55, 65, 35, 75, 85)), 4)
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(CountPassingGrades(c(0, 100, 0, 100)), 2)
#end_test_case

#@ Test Case
# sort_order: 100
# begin_test_case
testthat::expect_equal(CountPassingGrades(numeric(0)), 0)
#end_test_case