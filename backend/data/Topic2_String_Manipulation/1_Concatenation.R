#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: String Manipulation
# sort_order: 10
# title: Concatenation
# difficulty: 1

"--begin_description
You are given four strings `str1`, `str2`, `str3`, and `str4`.
Concatenate (join) these strings together using white space as separator. Return the results.

**Hint:** use the built-in `paste()` function
--end_description"

# begin_starter_code
Concatenate <- function(str1, str2, str3, str4) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(Concatenate("I", "love", "Rnold", ":)"), "I love Rnold :)")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(Concatenate("1", "2", "3", "4"), "1 2 3 4")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(Concatenate("_", "_", "_", "_"), "_ _ _ _")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(Concatenate("Trust", "the", "Natural", "Recursion"), "Trust the Natural Recursion")
#end_test_case