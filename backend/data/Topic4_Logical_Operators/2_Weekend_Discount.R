#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Logical Operators
# sort_order: 20
# title: Weekend Discount
# difficulty: 1

"--begin_description
You are given the current day of the week `today` as a string.
A store only has discounts on weekends.
Evaluate if there is a discount today and return the result.

You can assume that `today` has one of the following values:
`Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat`, `Sun`
--end_description"

# begin_starter_code
WeekendDiscount <- function(today) {

    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(FALSE, WeekendDiscount("Mon"))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(TRUE, WeekendDiscount("Sat"))
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(TRUE, WeekendDiscount("Sun"))
#end_test_case