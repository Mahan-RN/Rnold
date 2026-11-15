#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 60
# title: Filter Grades
# difficulty: 1

"--begin_description
You are given a vector of student grades `grades`.
Return the grades that are at least 50 but below 90.
--end_description"

# begin_starter_code
FilterGrades <- function(grades) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(FilterEvens(c()), 
                       c())
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(FilterGrades(49:70), 
                       50:70)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(FilterGrades(50:100), 
                       50:89)
#end_test_case
