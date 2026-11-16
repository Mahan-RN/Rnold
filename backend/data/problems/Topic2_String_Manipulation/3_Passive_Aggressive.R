#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: String Manipulation
# sort_order: 30
# title: Passive Aggressive
# difficulty: 1

"--begin_description
You are given two strings `str1` and `str2`.
Convert `str1` to all lower case and `str2` to all upper case. Then concatenate them and return the result.

**Hint:** you might find these helpful: `tolower()`, `toupper()`
--end_description"

# begin_starter_code
PassiveAggressive <- function(str1, str2) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(PassiveAggressive("", ""), " ")
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(PassiveAggressive("It’s fine I’ll just do it all myself", "LIKE USUAL"), "it’s fine i’ll just do it all myself LIKE USUAL")
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(PassiveAggressive("Yay,", "teamwork"), "yay, TEAMWORK")
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(PassiveAggressive("living the", "dream"), "living the DREAM")
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(PassiveAggressive("GOOD LUCK", "with that"), "good luck WITH THAT")
#end_test_case