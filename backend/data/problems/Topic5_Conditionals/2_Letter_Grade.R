#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 20
# title: Letter Grade
# difficulty: 1

"--begin_description
You are given a student grade `grade` as a number.
Return a string describing the grade, using the following format:
- `Invalid` if the grade is below 0 or greater than 100
- `A` for 90 and above
- `B` for 80 to 89
- `C` for 70 to 79
- `D` for 50 to 69
- `F` for 0 to 49
--end_description"

# begin_starter_code
LetterGrade <- function(grade) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(LetterGrade(101), "Invalid")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(LetterGrade(-1), "Invalid")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(LetterGrade(90), "A")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(LetterGrade(85), "B")
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(LetterGrade(75), "C")
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(LetterGrade(60), "D")
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(LetterGrade(25), "F")
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(LetterGrade(0), "F")
#end_test_case

#@ Test Case
# sort_order: 90
# begin_test_case
testthat::expect_equal(LetterGrade(100), "A")
#end_test_case