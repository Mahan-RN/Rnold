/*
  Rnold sample data: users, topics, problems, evaluation_cases, submissions

  Run with:
    psql -v ON_ERROR_STOP=1 -d <your_database> -f seed_rnold.sql

  Notes
  * Foreign keys are resolved by topic name and problem title, so no ids are hardcoded.
    The one exception is submissions.user_id, which uses the sample users' github_id.
  * Difficulty values follow the Difficulty IntEnum: 1 = EASY, 2 = MEDIUM, 3 = HARD.
  * evaluation_cases.code is a complete testthat assertion, evaluated after the
    learner's code in the same R environment. A failed expectation raises an R
    error and a passing one does not, so "ran without error" means "passed".
    Do not wrap these in stopifnot(): expect_*() returns its input invisibly,
    so stopifnot(expect_equal(f(x), y)) would fail correct answers whenever f(x)
    is not TRUE.
  * expect_equal() is used everywhere except Count Vowels, which uses
    expect_identical() because that problem requires an integer result.
  * evaluation_cases has only problem_id, code and sort_order, so each assertion
    carries its own expected value. sort_order is the position within the problem,
    and the pair (problem_id, sort_order) must be unique, so each problem numbers
    its cases 1, 2, 3 and so on without repeats.
  * The webR instance needs the testthat package installed.
  * topics.sort_order and problems.sort_order are required, and topics.sort_order
    is unique, so every row below has a value.
  * users.github_id is the primary key and normally comes from GitHub. The
    sample users use negative ids, which GitHub never issues, so a real account
    signing in through OAuth can never match a sample row and inherit its role.
    To remove only the sample users: DELETE FROM users WHERE github_id < 0;
    Their submissions go with them, because submissions.user_id is ON DELETE CASCADE.
  * users.role follows the Role IntEnum: 1 = USER, 2 = ADMIN. The model's default
    is applied by Python and not by the database, so raw SQL must always set it.
  * created_at and last_login have server defaults, but explicit values are used
    so the sample data has a spread of dates. last_login is never earlier than
    created_at. Sample emails use example.com, which is reserved for documentation.
  * submissions.status follows the Status IntEnum: 1 = ACCEPTED, 2 = WRONG_ANSWER,
    3 = ERROR. runtime_ms and code are required. created_at has a server default,
    but explicit values are used so each user has a believable attempt history.
    A submission is never dated before its user's created_at or after their last_login.
  * Run once on an empty database. A second run stops at the unique topic name, and
    ON_ERROR_STOP rolls the transaction back. To reset, uncomment the line below. CASCADE also empties submissions, because it references problems. Users
    are not touched.

  TRUNCATE evaluation_cases, problems, topics RESTART IDENTITY CASCADE;
*/

BEGIN;

/* ------------------------------------------------------------------ */
/* Users                                                               */
/* ------------------------------------------------------------------ */

/* role: 1 = USER, 2 = ADMIN (the Role IntEnum) */
INSERT INTO users (github_id, github_email, username, role, created_at, last_login) VALUES
  (-1, $$rnoldadmin@example.com$$, $$rnoldadmin$$, 2, now() - interval '180 days', now() - interval '1 hour'),
  (-2, $$tidytess@example.com$$, $$tidytess$$, 2, now() - interval '150 days', now() - interval '2 days'),
  (-3, $$vectorvic@example.com$$, $$vectorvic$$, 1, now() - interval '120 days', now() - interval '3 hours'),
  (-4, $$pipedream@example.com$$, $$pipedream$$, 1, now() - interval '100 days', now() - interval '10 days'),
  (-5, $$factorfran@example.com$$, $$factorfran$$, 1, now() - interval '75 days', now() - interval '36 hours'),
  (-6, $$narmnora@example.com$$, $$narmnora$$, 1, now() - interval '60 days', now() - interval '5 days'),
  (-7, $$lazyevallee@example.com$$, $$lazyevallee$$, 1, now() - interval '45 days', now() - interval '12 hours'),
  /* Edge case: has not logged in since signing up (last_login equals created_at) */
  (-8, $$forloopfinn@example.com$$, $$forloopfinn$$, 1, now() - interval '30 days', now() - interval '30 days'),
  /* Edge case: signed up today */
  (-9, $$newbieneil@example.com$$, $$newbieneil$$, 1, now() - interval '3 hours', now() - interval '3 hours'),
  /* Edge case: 39 character username, the GitHub maximum */
  (-10, $$longusernamelongusernamelongusername123@example.com$$, $$longusernamelongusernamelongusername123$$, 1, now() - interval '20 days', now() - interval '1 day')
ON CONFLICT (github_id) DO NOTHING;

/* ------------------------------------------------------------------ */
/* Topics                                                              */
/* ------------------------------------------------------------------ */

INSERT INTO topics (name, description, sort_order) VALUES
(
  $$Boolean Logic$$,
  $$Get comfortable with TRUE and FALSE, comparison operators, the modulo operator, and combining conditions with & and |.$$,
  1
),
(
  $$Arrays$$,
  $$Work with numeric vectors: arithmetic, summaries, indexing, and building new vectors from old ones.$$,
  2
),
(
  $$Strings$$,
  $$Manipulate character data using functions such as nchar, substr, strsplit, paste, and regular expressions.$$,
  3
),
(
  /* Edge case for the frontend: a topic with no problems */
  $$Data Frames$$,
  $$Coming soon. Practice creating, filtering, and summarising tabular data.$$,
  4
);

/* ------------------------------------------------------------------ */
/* Problems                                                            */
/* ------------------------------------------------------------------ */

INSERT INTO problems (topic_id, sort_order, title, description, difficulty, starter_code) VALUES

/* ---- Boolean Logic ---- */
(
  (SELECT id FROM topics WHERE name = $$Boolean Logic$$),
  1,
  $$Is Even$$,
  $$Write a function `is_even(n)` that returns `TRUE` if the whole number `n` is even and `FALSE` otherwise.

**Examples**

```r
is_even(4)  # TRUE
is_even(7)  # FALSE
```

**Notes**

* `n` is a single whole number and may be zero or negative.$$,
  1,
  $$is_even <- function(n) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Boolean Logic$$),
  2,
  $$Leap Year$$,
  $$Write a function `is_leap_year(year)` that returns `TRUE` if `year` is a leap year in the Gregorian calendar.

A year is a leap year if it is divisible by 4, except for years divisible by 100, which are leap years only if they are also divisible by 400.

**Examples**

```r
is_leap_year(2024)  # TRUE
is_leap_year(1900)  # FALSE
is_leap_year(2000)  # TRUE
```$$,
  2,
  $$is_leap_year <- function(year) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Boolean Logic$$),
  3,
  $$Valid Triangle$$,
  $$Write a function `is_valid_triangle(a, b, c)` that returns `TRUE` if three side lengths can form a triangle.

The sum of any two sides must be strictly greater than the third side. Sides that are zero or negative never form a triangle.

**Examples**

```r
is_valid_triangle(3, 4, 5)  # TRUE
is_valid_triangle(1, 2, 3)  # FALSE
```

**Notes**

* A degenerate triangle, where two sides add up exactly to the third, is not valid.$$,
  2,
  $$is_valid_triangle <- function(a, b, c) {
  # Your code here
}
$$
),

/* ---- Arrays ---- */
(
  (SELECT id FROM topics WHERE name = $$Arrays$$),
  1,
  $$Sum of Squares$$,
  $$Write a function `sum_of_squares(x)` that returns the sum of the squares of every element in the numeric vector `x`.

**Examples**

```r
sum_of_squares(c(1, 2, 3))  # 14
sum_of_squares(c(-2, 2))    # 8
```

**Notes**

* The sum of an empty vector is `0`.$$,
  1,
  $$sum_of_squares <- function(x) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Arrays$$),
  2,
  $$Running Total$$,
  $$Write a function `running_total(x)` that returns a vector where each element is the sum of all elements of `x` up to and including that position.

Try to solve this without calling `cumsum()`.

**Examples**

```r
running_total(c(1, 2, 3, 4))  # c(1, 3, 6, 10)
running_total(c(5, -2, 4))    # c(5, 3, 7)
```

**Notes**

* For an empty input, return an empty numeric vector.$$,
  1,
  $$running_total <- function(x) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Arrays$$),
  3,
  $$Second Largest$$,
  $$Write a function `second_largest(x)` that returns the second largest distinct value in the numeric vector `x`.

If `x` has fewer than two distinct values, return `NULL`.

**Examples**

```r
second_largest(c(3, 1, 4, 1, 5))  # 4
second_largest(c(9, 9, 8))        # 8
second_largest(c(5, 5, 5))        # NULL
```$$,
  2,
  $$second_largest <- function(x) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Arrays$$),
  4,
  $$Rotate Vector Left$$,
  $$Write a function `rotate_left(x, k)` that moves every element of `x` left by `k` positions, wrapping the elements that fall off the front around to the back.

**Examples**

```r
rotate_left(c(1, 2, 3, 4, 5), 2)  # c(3, 4, 5, 1, 2)
rotate_left(c(1, 2, 3), 4)        # c(2, 3, 1)
```

**Notes**

* `k` may be larger than the length of `x`.
* A negative `k` rotates to the right instead.
* An empty vector should be returned unchanged.$$,
  2,
  $$rotate_left <- function(x, k) {
  # Your code here
}
$$
),

/* ---- Strings ---- */
(
  (SELECT id FROM topics WHERE name = $$Strings$$),
  1,
  $$Reverse a String$$,
  $$Write a function `reverse_string(s)` that returns the single string `s` with its characters in reverse order.

**Examples**

```r
reverse_string("hello")  # "olleh"
reverse_string("R")      # "R"
```

**Notes**

* An empty string should return an empty string.$$,
  1,
  $$reverse_string <- function(s) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Strings$$),
  2,
  $$Count Vowels$$,
  $$Write a function `count_vowels(s)` that returns the number of vowels (`a`, `e`, `i`, `o`, `u`) in the single string `s`. Ignore case.

Return an **integer**, for example `2L` rather than `2`.

**Examples**

```r
count_vowels("hello")      # 2L
count_vowels("RHYTHM")     # 0L
count_vowels("Education")  # 5L
```$$,
  1,
  $$count_vowels <- function(s) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Strings$$),
  3,
  $$Palindrome Check$$,
  $$Write a function `is_palindrome(s)` that returns `TRUE` if the string `s` reads the same forwards and backwards.

Ignore upper and lower case, and ignore every character that is not a letter or a digit.

**Examples**

```r
is_palindrome("racecar")                         # TRUE
is_palindrome("A man, a plan, a canal: Panama")  # TRUE
is_palindrome("hello")                           # FALSE
```

**Notes**

* An empty string counts as a palindrome.$$,
  2,
  $$is_palindrome <- function(s) {
  # Your code here
}
$$
),
(
  (SELECT id FROM topics WHERE name = $$Strings$$),
  4,
  $$Caesar Cipher$$,
  $$Write a function `caesar_cipher(s, shift)` that shifts every letter in `s` by `shift` positions through the alphabet, wrapping around from `z` back to `a`.

Upper and lower case letters keep their case. Characters that are not letters are left unchanged.

**Examples**

```r
caesar_cipher("abc", 1)            # "bcd"
caesar_cipher("xyz", 3)            # "abc"
caesar_cipher("Hello, World!", 5)  # "Mjqqt, Btwqi!"
```

**Notes**

* `shift` may be negative or larger than 26.$$,
  3,
  $$caesar_cipher <- function(s, shift) {
  # Your code here
}
$$
),
(
  /* Edge case: a problem nobody has attempted */
  (SELECT id FROM topics WHERE name = $$Strings$$),
  5,
  $$Anagram Check$$,
  $$Write a function `are_anagrams(a, b)` that returns `TRUE` if the strings `a` and `b` contain exactly the same letters, ignoring case.

**Examples**

```r
are_anagrams("listen", "silent")  # TRUE
are_anagrams("hello", "world")    # FALSE
```$$,
  2,
  $$are_anagrams <- function(a, b) {
  # Your code here
}
$$
);

/* ------------------------------------------------------------------ */
/* Evaluation cases                                                    */
/* ------------------------------------------------------------------ */

INSERT INTO evaluation_cases (problem_id, sort_order, code)
SELECT p.id, v.sort_order, v.code
FROM (VALUES

  /* Is Even */
  ($$Is Even$$, 1, $$testthat::expect_equal(is_even(4), TRUE)$$),
  ($$Is Even$$, 2, $$testthat::expect_equal(is_even(7), FALSE)$$),
  ($$Is Even$$, 3, $$testthat::expect_equal(is_even(0), TRUE)$$),
  ($$Is Even$$, 4, $$testthat::expect_equal(is_even(-3), FALSE)$$),
  ($$Is Even$$, 5, $$testthat::expect_equal(is_even(-10), TRUE)$$),

  /* Leap Year */
  ($$Leap Year$$, 1, $$testthat::expect_equal(is_leap_year(2024), TRUE)$$),
  ($$Leap Year$$, 2, $$testthat::expect_equal(is_leap_year(2023), FALSE)$$),
  ($$Leap Year$$, 3, $$testthat::expect_equal(is_leap_year(1900), FALSE)$$),
  ($$Leap Year$$, 4, $$testthat::expect_equal(is_leap_year(2000), TRUE)$$),
  ($$Leap Year$$, 5, $$testthat::expect_equal(is_leap_year(2100), FALSE)$$),

  /* Valid Triangle */
  ($$Valid Triangle$$, 1, $$testthat::expect_equal(is_valid_triangle(3, 4, 5), TRUE)$$),
  ($$Valid Triangle$$, 2, $$testthat::expect_equal(is_valid_triangle(1, 2, 3), FALSE)$$),
  ($$Valid Triangle$$, 3, $$testthat::expect_equal(is_valid_triangle(5, 1, 1), FALSE)$$),
  ($$Valid Triangle$$, 4, $$testthat::expect_equal(is_valid_triangle(0, 4, 4), FALSE)$$),
  ($$Valid Triangle$$, 5, $$testthat::expect_equal(is_valid_triangle(2, 2, 2), TRUE)$$),

  /* Sum of Squares */
  ($$Sum of Squares$$, 1, $$testthat::expect_equal(sum_of_squares(c(1, 2, 3)), 14)$$),
  ($$Sum of Squares$$, 2, $$testthat::expect_equal(sum_of_squares(c(-2, 2)), 8)$$),
  ($$Sum of Squares$$, 3, $$testthat::expect_equal(sum_of_squares(5), 25)$$),
  ($$Sum of Squares$$, 4, $$testthat::expect_equal(sum_of_squares(numeric(0)), 0)$$),

  /* Running Total */
  ($$Running Total$$, 1, $$testthat::expect_equal(running_total(c(1, 2, 3, 4)), c(1, 3, 6, 10))$$),
  ($$Running Total$$, 2, $$testthat::expect_equal(running_total(c(5, -2, 4)), c(5, 3, 7))$$),
  ($$Running Total$$, 3, $$testthat::expect_equal(running_total(c(7)), 7)$$),
  ($$Running Total$$, 4, $$testthat::expect_equal(running_total(numeric(0)), numeric(0))$$),

  /* Second Largest */
  ($$Second Largest$$, 1, $$testthat::expect_equal(second_largest(c(3, 1, 4, 1, 5)), 4)$$),
  ($$Second Largest$$, 2, $$testthat::expect_equal(second_largest(c(10, 20)), 10)$$),
  ($$Second Largest$$, 3, $$testthat::expect_equal(second_largest(c(5, 5, 5)), NULL)$$),
  ($$Second Largest$$, 4, $$testthat::expect_equal(second_largest(c(-1, -5, -3)), -3)$$),
  ($$Second Largest$$, 5, $$testthat::expect_equal(second_largest(c(2, 9, 9, 8)), 8)$$),

  /* Rotate Vector Left */
  ($$Rotate Vector Left$$, 1, $$testthat::expect_equal(rotate_left(c(1, 2, 3, 4, 5), 2), c(3, 4, 5, 1, 2))$$),
  ($$Rotate Vector Left$$, 2, $$testthat::expect_equal(rotate_left(c(1, 2, 3), 4), c(2, 3, 1))$$),
  ($$Rotate Vector Left$$, 3, $$testthat::expect_equal(rotate_left(c(1, 2, 3, 4), -1), c(4, 1, 2, 3))$$),
  ($$Rotate Vector Left$$, 4, $$testthat::expect_equal(rotate_left(c(9), 5), 9)$$),
  ($$Rotate Vector Left$$, 5, $$testthat::expect_equal(rotate_left(numeric(0), 3), numeric(0))$$),

  /* Reverse a String */
  ($$Reverse a String$$, 1, $$testthat::expect_equal(reverse_string("hello"), "olleh")$$),
  ($$Reverse a String$$, 2, $$testthat::expect_equal(reverse_string("R"), "R")$$),
  ($$Reverse a String$$, 3, $$testthat::expect_equal(reverse_string(""), "")$$),
  ($$Reverse a String$$, 4, $$testthat::expect_equal(reverse_string("A man a plan"), "nalp a nam A")$$),

  /* Count Vowels */
  ($$Count Vowels$$, 1, $$testthat::expect_identical(count_vowels("hello"), 2L)$$),
  ($$Count Vowels$$, 2, $$testthat::expect_identical(count_vowels("RHYTHM"), 0L)$$),
  ($$Count Vowels$$, 3, $$testthat::expect_identical(count_vowels("Education"), 5L)$$),
  ($$Count Vowels$$, 4, $$testthat::expect_identical(count_vowels(""), 0L)$$),

  /* Palindrome Check */
  ($$Palindrome Check$$, 1, $$testthat::expect_equal(is_palindrome("racecar"), TRUE)$$),
  ($$Palindrome Check$$, 2, $$testthat::expect_equal(is_palindrome("hello"), FALSE)$$),
  ($$Palindrome Check$$, 3, $$testthat::expect_equal(is_palindrome("A man, a plan, a canal: Panama"), TRUE)$$),
  ($$Palindrome Check$$, 4, $$testthat::expect_equal(is_palindrome("No lemon, no melon"), TRUE)$$),
  ($$Palindrome Check$$, 5, $$testthat::expect_equal(is_palindrome(""), TRUE)$$),

  /* Caesar Cipher */
  ($$Caesar Cipher$$, 1, $$testthat::expect_equal(caesar_cipher("abc", 1), "bcd")$$),
  ($$Caesar Cipher$$, 2, $$testthat::expect_equal(caesar_cipher("xyz", 3), "abc")$$),
  ($$Caesar Cipher$$, 3, $$testthat::expect_equal(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")$$),
  ($$Caesar Cipher$$, 4, $$testthat::expect_equal(caesar_cipher("abc", -1), "zab")$$),
  ($$Caesar Cipher$$, 5, $$testthat::expect_equal(caesar_cipher("abc", 27), "bcd")$$),

  /* Anagram Check */
  ($$Anagram Check$$, 1, $$testthat::expect_equal(are_anagrams("listen", "silent"), TRUE)$$),
  ($$Anagram Check$$, 2, $$testthat::expect_equal(are_anagrams("hello", "world"), FALSE)$$)

) AS v(title, sort_order, code)
JOIN problems p ON p.title = v.title;

/* ------------------------------------------------------------------ */
/* Submissions                                                         */
/* status: 1 = ACCEPTED, 2 = WRONG_ANSWER, 3 = ERROR (the Status IntEnum) */
/* Covers: failed attempts followed by a pass, a problem resubmitted   */
/* after it was already solved, a problem attempted but never solved,  */
/* and users with no submissions (forloopfinn, newbieneil).            */
/* ------------------------------------------------------------------ */

INSERT INTO submissions (user_id, problem_id, status, runtime_ms, created_at, code)
SELECT v.user_id, p.id, v.status, v.runtime_ms, v.created_at, v.code
FROM (VALUES

  /* rnoldadmin: smoke tests of the first two problems */
  (-1, $$Is Even$$, 1, 41, now() - interval '170 days', $$is_even <- function(n) {
  n %% 2 == 0
}
$$),
  (-1, $$Leap Year$$, 1, 45, now() - interval '169 days 23 hours', $$is_leap_year <- function(year) {
  (year %% 4 == 0 & year %% 100 != 0) | year %% 400 == 0
}
$$),

  /* tidytess */
  (-2, $$Is Even$$, 1, 39, now() - interval '140 days', $$is_even <- function(n) {
  n %% 2 == 0
}
$$),
  (-2, $$Leap Year$$, 2, 58, now() - interval '139 days 23 hours', $$is_leap_year <- function(year) {
  year %% 4 == 0
}
$$),
  (-2, $$Leap Year$$, 1, 47, now() - interval '139 days 22 hours', $$is_leap_year <- function(year) {
  (year %% 4 == 0 & year %% 100 != 0) | year %% 400 == 0
}
$$),
  (-2, $$Valid Triangle$$, 2, 63, now() - interval '120 days', $$is_valid_triangle <- function(a, b, c) {
  a + b >= c && a + c >= b && b + c >= a
}
$$),
  (-2, $$Valid Triangle$$, 1, 51, now() - interval '119 days 23 hours', $$is_valid_triangle <- function(a, b, c) {
  a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a
}
$$),
  /* Edge case: ERROR from a package that is not installed */
  (-2, $$Reverse a String$$, 3, 17, now() - interval '60 days', $$reverse_string <- function(s) {
  stringi::stri_reverse(s)
}
$$),
  (-2, $$Reverse a String$$, 1, 55, now() - interval '59 days 23 hours', $$reverse_string <- function(s) {
  paste(rev(strsplit(s, "")[[1]]), collapse = "")
}
$$),

  /* vectorvic: works through the Arrays topic, then tries Strings */
  (-3, $$Is Even$$, 1, 36, now() - interval '110 days', $$is_even <- function(n) {
  n %% 2 == 0
}
$$),
  /* Classic bug: 1:length(x) misbehaves on an empty vector */
  (-3, $$Sum of Squares$$, 2, 59, now() - interval '100 days', $$sum_of_squares <- function(x) {
  total <- 0
  for (i in 1:length(x)) {
    total <- total + x[i]^2
  }
  total
}
$$),
  (-3, $$Sum of Squares$$, 1, 33, now() - interval '99 days 23 hours', $$sum_of_squares <- function(x) {
  sum(x^2)
}
$$),
  (-3, $$Running Total$$, 1, 90, now() - interval '95 days', $$running_total <- function(x) {
  out <- numeric(length(x))
  total <- 0
  for (i in seq_along(x)) {
    total <- total + x[i]
    out[i] <- total
  }
  out
}
$$),
  /* Edge case: resubmitting a problem that was already solved */
  (-3, $$Running Total$$, 1, 38, now() - interval '94 days', $$running_total <- function(x) {
  cumsum(x)
}
$$),
  (-3, $$Second Largest$$, 2, 64, now() - interval '80 days', $$second_largest <- function(x) {
  sort(x, decreasing = TRUE)[2]
}
$$),
  (-3, $$Second Largest$$, 1, 49, now() - interval '79 days 22 hours', $$second_largest <- function(x) {
  u <- sort(unique(x), decreasing = TRUE)
  if (length(u) < 2) {
    return(NULL)
  }
  u[2]
}
$$),
  (-3, $$Rotate Vector Left$$, 2, 71, now() - interval '60 days', $$rotate_left <- function(x, k) {
  c(x[(k + 1):length(x)], x[1:k])
}
$$),
  (-3, $$Rotate Vector Left$$, 1, 54, now() - interval '59 days 20 hours', $$rotate_left <- function(x, k) {
  n <- length(x)
  if (n == 0) {
    return(x)
  }
  x[(seq_len(n) + k - 1) %% n + 1]
}
$$),
  (-3, $$Caesar Cipher$$, 1, 120, now() - interval '2 days', $$caesar_cipher <- function(s, shift) {
  shift_char <- function(ch) {
    if (ch %in% letters) {
      letters[(match(ch, letters) - 1 + shift) %% 26 + 1]
    } else if (ch %in% LETTERS) {
      LETTERS[(match(ch, LETTERS) - 1 + shift) %% 26 + 1]
    } else {
      ch
    }
  }
  chars <- strsplit(s, "")[[1]]
  paste(vapply(chars, shift_char, character(1), USE.NAMES = FALSE), collapse = "")
}
$$),

  /* pipedream: three attempts at the first problem */
  (-4, $$Is Even$$, 3, 9, now() - interval '90 days', $$is_even <- function(n) {
  if (mod(n, 2) == 0) TRUE else FALSE
}
$$),
  /* Edge case: infinite loop on negative input, recorded as an ERROR at 5000 ms */
  (-4, $$Is Even$$, 3, 5000, now() - interval '89 days 23 hours 40 minutes', $$is_even <- function(n) {
  while (n != 0 && n != 1) {
    n <- n - 2
  }
  n == 0
}
$$),
  (-4, $$Is Even$$, 1, 44, now() - interval '89 days 23 hours', $$is_even <- function(n) {
  n %% 2 == 0
}
$$),
  /* Case sensitive match misses the capital E in "Education" */
  (-4, $$Count Vowels$$, 2, 66, now() - interval '70 days', $$count_vowels <- function(s) {
  nchar(gsub("[^aeiou]", "", s))
}
$$),
  (-4, $$Count Vowels$$, 1, 58, now() - interval '69 days 22 hours', $$count_vowels <- function(s) {
  chars <- strsplit(tolower(s), "")[[1]]
  sum(chars %in% c("a", "e", "i", "o", "u"))
}
$$),

  /* factorfran */
  (-5, $$Is Even$$, 1, 40, now() - interval '70 days', $$is_even <- function(n) {
  n %% 2 == 0
}
$$),
  (-5, $$Palindrome Check$$, 2, 77, now() - interval '40 days', $$is_palindrome <- function(s) {
  s == paste(rev(strsplit(s, "")[[1]]), collapse = "")
}
$$),
  (-5, $$Palindrome Check$$, 1, 69, now() - interval '39 days 23 hours', $$is_palindrome <- function(s) {
  cleaned <- tolower(gsub("[^A-Za-z0-9]", "", s))
  cleaned == paste(rev(strsplit(cleaned, "")[[1]]), collapse = "")
}
$$),
  /* Edge case: attempted but never solved */
  (-5, $$Caesar Cipher$$, 2, 95, now() - interval '30 days', $$caesar_cipher <- function(s, shift) {
  codes <- utf8ToInt(s) + shift
  intToUtf8(codes)
}
$$),

  /* narmnora */
  (-6, $$Sum of Squares$$, 1, 35, now() - interval '50 days', $$sum_of_squares <- function(x) {
  sum(x^2)
}
$$),
  (-6, $$Running Total$$, 2, 82, now() - interval '48 days', $$running_total <- function(x) {
  c(x[1], x[-1] + x[-length(x)])
}
$$),
  (-6, $$Running Total$$, 1, 79, now() - interval '47 days 23 hours', $$running_total <- function(x) {
  out <- numeric(length(x))
  total <- 0
  for (i in seq_along(x)) {
    total <- total + x[i]
    out[i] <- total
  }
  out
}
$$),

  /* lazyevallee: solves each problem on the first attempt */
  (-7, $$Is Even$$, 1, 42, now() - interval '40 days', $$is_even <- function(n) {
  n %% 2 == 0
}
$$),
  (-7, $$Leap Year$$, 1, 46, now() - interval '39 days', $$is_leap_year <- function(year) {
  (year %% 4 == 0 & year %% 100 != 0) | year %% 400 == 0
}
$$),
  (-7, $$Valid Triangle$$, 1, 50, now() - interval '38 days', $$is_valid_triangle <- function(a, b, c) {
  a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a
}
$$),
  (-7, $$Reverse a String$$, 1, 60, now() - interval '20 hours', $$reverse_string <- function(s) {
  paste(rev(strsplit(s, "")[[1]]), collapse = "")
}
$$),

  /* longusernamelongusernamelongusername123 */
  /* rev() on a single string returns it unchanged */
  (-10, $$Reverse a String$$, 2, 58, now() - interval '10 days', $$reverse_string <- function(s) {
  rev(s)
}
$$),
  (-10, $$Reverse a String$$, 1, 60, now() - interval '9 days 23 hours', $$reverse_string <- function(s) {
  paste(rev(strsplit(s, "")[[1]]), collapse = "")
}
$$),
  (-10, $$Palindrome Check$$, 1, 71, now() - interval '5 days', $$is_palindrome <- function(s) {
  cleaned <- tolower(gsub("[^A-Za-z0-9]", "", s))
  cleaned == paste(rev(strsplit(cleaned, "")[[1]]), collapse = "")
}
$$)

) AS v(user_id, title, status, runtime_ms, created_at, code)
JOIN problems p ON p.title = v.title
ORDER BY v.created_at;

COMMIT;

/* Quick sanity check */
SELECT t.name AS topic, p.sort_order, p.title, p.difficulty,
       COUNT(ec.id) AS evaluation_cases,
       (SELECT COUNT(*) FROM submissions s WHERE s.problem_id = p.id) AS submissions
FROM topics t
LEFT JOIN problems p ON p.topic_id = t.id
LEFT JOIN evaluation_cases ec ON ec.problem_id = p.id
GROUP BY t.name, t.sort_order, p.id, p.sort_order, p.title, p.difficulty
ORDER BY t.sort_order, p.sort_order NULLS LAST;

/* Users by role */
SELECT role, COUNT(*) AS users FROM users GROUP BY role ORDER BY role;

/* Submissions by status: 1 = ACCEPTED, 2 = WRONG_ANSWER, 3 = ERROR */
SELECT status, COUNT(*) AS submissions FROM submissions GROUP BY status ORDER BY status;
