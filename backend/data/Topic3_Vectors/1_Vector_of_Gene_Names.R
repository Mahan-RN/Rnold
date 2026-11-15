#@ Preamble
# Problem Template for Rnold
# Install `testthat` package if you don't already have it
# install.packages("testthat")
# Note: all lines in the preamble section will be ignored by Rnold

#@ Problem
# topic_name: Vectors
# sort_order: 10
# title: Vector of Gene Names
# difficulty: 1

"--begin_description
You are given the names of 3 genes: `gene1`, `gene2`, `gene3`.
Create a vector to hold these gene names, in the correct order. Return the result
--end_description"

# begin_starter_code
VectorizeGenes <- function(gene1, gene2, gene3) {
    
    return(...)
}
# end_starter_code

#@ Test Case
# sort_order: 10
# begin_test_case
testthat::expect_equal(c("PAX1", "PAX2", "PAX3"), VectorizeGenes("PAX1", "PAX2", "PAX3"))
#end_test_case

#@ Test Case
# sort_order: 20
# begin_test_case
testthat::expect_equal(c("TLR1", "TLR2", "TLR3"), VectorizeGenes("TLR1", "TLR2", "TLR3"))
#end_test_case