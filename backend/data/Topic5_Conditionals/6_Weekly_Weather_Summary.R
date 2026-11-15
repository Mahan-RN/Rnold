#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 60
# title: Weekly Weather Summary
# difficulty: 3

"--begin_description
You are given a numeric vector of daily temperatures in degrees Celsius `temps`.

Calculate the average temperature and classify it as follows:
- `Hot` if the average is 25 or above.
- `Mild` if the average is at least 15 but below 25.
- `Cold` if the average is below 15.

If any individual temperature in `temps` is below 0, append `with frost` to the resulting label.

Return the final classification as a string.
--end_description"

# begin_starter_code
WeatherSummary <- function(temps) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(
    WeatherSummary(c(26, 28, 30)),
    "Hot"
)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(
    WeatherSummary(c(15, 20, 24)),
    "Mild"
)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(
    WeatherSummary(c(5, 10, 14)),
    "Cold"
)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(
    WeatherSummary(c(-2, 10, 12)),
    "Cold with frost"
)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(
    WeatherSummary(c(-5, 25, 30)),
    "Mild with frost"
)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(
    WeatherSummary(c(0, 15, 20)),
    "Cold"
)
#end_test_case