#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Conditionals
# sort_order: 50
# title: Shipping Cost
# difficulty: 2

"--begin_description
You are given the weight of a parcel in kilograms `weight` and a boolean `express` indicating whether express shipping has been requested.

Calculate and return the shipping cost according to the following rules:
- The base cost is `5` for parcels weighing up to 1 kg.
- The base cost is `8` for parcels weighing more than 1 kg and up to 5 kg.
- For parcels weighing more than 5 kg, the base cost is `8` plus `2` for each additional kilogram (or fraction thereof) above 5 kg.
- If `express` is `TRUE`, multiply the base cost by `1.5`.

--end_description"

# begin_starter_code
ShippingCost <- function(weight, express) {

    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(ShippingCost(0.5, FALSE), 5)
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(ShippingCost(1, FALSE), 5)
#end_test_case

#@ Test Case
# sort_order: 30
# begin_test_case
testthat::expect_equal(ShippingCost(3, FALSE), 8)
#end_test_case

#@ Test Case
# sort_order: 40
# begin_test_case
testthat::expect_equal(ShippingCost(5, FALSE), 8)
#end_test_case

#@ Test Case
# sort_order: 50
# begin_test_case
testthat::expect_equal(ShippingCost(6, FALSE), 10)
#end_test_case

#@ Test Case
# sort_order: 60
# begin_test_case
testthat::expect_equal(ShippingCost(10, FALSE), 18)
#end_test_case

#@ Test Case
# sort_order: 70
# begin_test_case
testthat::expect_equal(ShippingCost(2, TRUE), 12)
#end_test_case

#@ Test Case
# sort_order: 80
# begin_test_case
testthat::expect_equal(ShippingCost(6, TRUE), 15)
#end_test_case