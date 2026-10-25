/*
  Rnold sample data: topics, problems, test_cases

  Run with:
    psql -v ON_ERROR_STOP=1 -d <your_database> -f seed_rnold.sql

  Notes
  * Foreign keys are resolved by topic name and problem title, so no ids are hardcoded.
  * Difficulty values follow the Difficulty IntEnum: 1 = EASY, 2 = MEDIUM, 3 = HARD.
  * test_cases.code is an R expression evaluated after the learner's code.
    expected_output is the canonical deparse() form of the correct result.
  * Run once on an empty database. test_cases has no unique constraint, so a
    second run would duplicate them. To reset, uncomment the line below.
    CASCADE also empties submissions, because it references problems.

  TRUNCATE test_cases, problems, topics RESTART IDENTITY CASCADE;
*/

BEGIN;

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
  /* Edge case for the frontend: a topic with no problems and no sort order */
  $$Data Frames$$,
  $$Coming soon. Practice creating, filtering, and summarising tabular data.$$,
  NULL
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
  /* Edge case for the frontend: a draft problem with no sort order */
  (SELECT id FROM topics WHERE name = $$Strings$$),
  NULL,
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
/* Test cases                                                          */
/* The first two cases of each problem are visible, the rest hidden.   */
/* ------------------------------------------------------------------ */

INSERT INTO test_cases (problem_id, sort_order, code, expected_output, is_hidden)
SELECT p.id, v.sort_order, v.code, v.expected_output, v.is_hidden
FROM (VALUES

  /* Is Even */
  ($$Is Even$$, 1, $$is_even(4)$$,  $$TRUE$$,  FALSE),
  ($$Is Even$$, 2, $$is_even(7)$$,  $$FALSE$$, FALSE),
  ($$Is Even$$, 3, $$is_even(0)$$,  $$TRUE$$,  TRUE),
  ($$Is Even$$, 4, $$is_even(-3)$$, $$FALSE$$, TRUE),
  ($$Is Even$$, 5, $$is_even(-10)$$, $$TRUE$$, TRUE),

  /* Leap Year */
  ($$Leap Year$$, 1, $$is_leap_year(2024)$$, $$TRUE$$,  FALSE),
  ($$Leap Year$$, 2, $$is_leap_year(2023)$$, $$FALSE$$, FALSE),
  ($$Leap Year$$, 3, $$is_leap_year(1900)$$, $$FALSE$$, TRUE),
  ($$Leap Year$$, 4, $$is_leap_year(2000)$$, $$TRUE$$,  TRUE),
  ($$Leap Year$$, 5, $$is_leap_year(2100)$$, $$FALSE$$, TRUE),

  /* Valid Triangle */
  ($$Valid Triangle$$, 1, $$is_valid_triangle(3, 4, 5)$$, $$TRUE$$,  FALSE),
  ($$Valid Triangle$$, 2, $$is_valid_triangle(1, 2, 3)$$, $$FALSE$$, FALSE),
  ($$Valid Triangle$$, 3, $$is_valid_triangle(5, 1, 1)$$, $$FALSE$$, TRUE),
  ($$Valid Triangle$$, 4, $$is_valid_triangle(0, 4, 4)$$, $$FALSE$$, TRUE),
  ($$Valid Triangle$$, 5, $$is_valid_triangle(2, 2, 2)$$, $$TRUE$$,  TRUE),

  /* Sum of Squares */
  ($$Sum of Squares$$, 1, $$sum_of_squares(c(1, 2, 3))$$, $$14$$, FALSE),
  ($$Sum of Squares$$, 2, $$sum_of_squares(c(-2, 2))$$,   $$8$$,  FALSE),
  ($$Sum of Squares$$, 3, $$sum_of_squares(5)$$,          $$25$$, TRUE),
  ($$Sum of Squares$$, 4, $$sum_of_squares(numeric(0))$$, $$0$$,  TRUE),

  /* Running Total */
  ($$Running Total$$, 1, $$running_total(c(1, 2, 3, 4))$$, $$c(1, 3, 6, 10)$$, FALSE),
  ($$Running Total$$, 2, $$running_total(c(5, -2, 4))$$,   $$c(5, 3, 7)$$,     FALSE),
  ($$Running Total$$, 3, $$running_total(c(7))$$,          $$7$$,              TRUE),
  ($$Running Total$$, 4, $$running_total(numeric(0))$$,    $$numeric(0)$$,     TRUE),

  /* Second Largest */
  ($$Second Largest$$, 1, $$second_largest(c(3, 1, 4, 1, 5))$$, $$4$$,    FALSE),
  ($$Second Largest$$, 2, $$second_largest(c(10, 20))$$,        $$10$$,   FALSE),
  ($$Second Largest$$, 3, $$second_largest(c(5, 5, 5))$$,       $$NULL$$, TRUE),
  ($$Second Largest$$, 4, $$second_largest(c(-1, -5, -3))$$,    $$-3$$,   TRUE),
  ($$Second Largest$$, 5, $$second_largest(c(2, 9, 9, 8))$$,    $$8$$,    TRUE),

  /* Rotate Vector Left */
  ($$Rotate Vector Left$$, 1, $$rotate_left(c(1, 2, 3, 4, 5), 2)$$, $$c(3, 4, 5, 1, 2)$$, FALSE),
  ($$Rotate Vector Left$$, 2, $$rotate_left(c(1, 2, 3), 4)$$,       $$c(2, 3, 1)$$,       FALSE),
  ($$Rotate Vector Left$$, 3, $$rotate_left(c(1, 2, 3, 4), -1)$$,   $$c(4, 1, 2, 3)$$,    TRUE),
  ($$Rotate Vector Left$$, 4, $$rotate_left(c(9), 5)$$,             $$9$$,                TRUE),
  ($$Rotate Vector Left$$, 5, $$rotate_left(numeric(0), 3)$$,       $$numeric(0)$$,       TRUE),

  /* Reverse a String */
  ($$Reverse a String$$, 1, $$reverse_string("hello")$$,        $$"olleh"$$,        FALSE),
  ($$Reverse a String$$, 2, $$reverse_string("R")$$,            $$"R"$$,            FALSE),
  ($$Reverse a String$$, 3, $$reverse_string("")$$,             $$""$$,             TRUE),
  ($$Reverse a String$$, 4, $$reverse_string("A man a plan")$$, $$"nalp a nam A"$$, TRUE),

  /* Count Vowels */
  ($$Count Vowels$$, 1, $$count_vowels("hello")$$,     $$2L$$, FALSE),
  ($$Count Vowels$$, 2, $$count_vowels("RHYTHM")$$,    $$0L$$, FALSE),
  ($$Count Vowels$$, 3, $$count_vowels("Education")$$, $$5L$$, TRUE),
  ($$Count Vowels$$, 4, $$count_vowels("")$$,          $$0L$$, TRUE),

  /* Palindrome Check */
  ($$Palindrome Check$$, 1, $$is_palindrome("racecar")$$,                         $$TRUE$$,  FALSE),
  ($$Palindrome Check$$, 2, $$is_palindrome("hello")$$,                           $$FALSE$$, FALSE),
  ($$Palindrome Check$$, 3, $$is_palindrome("A man, a plan, a canal: Panama")$$,  $$TRUE$$,  TRUE),
  ($$Palindrome Check$$, 4, $$is_palindrome("No lemon, no melon")$$,              $$TRUE$$,  TRUE),
  ($$Palindrome Check$$, 5, $$is_palindrome("")$$,                                $$TRUE$$,  TRUE),

  /* Caesar Cipher */
  ($$Caesar Cipher$$, 1, $$caesar_cipher("abc", 1)$$,           $$"bcd"$$,           FALSE),
  ($$Caesar Cipher$$, 2, $$caesar_cipher("xyz", 3)$$,           $$"abc"$$,           FALSE),
  ($$Caesar Cipher$$, 3, $$caesar_cipher("Hello, World!", 5)$$, $$"Mjqqt, Btwqi!"$$, TRUE),
  ($$Caesar Cipher$$, 4, $$caesar_cipher("abc", -1)$$,          $$"zab"$$,           TRUE),
  ($$Caesar Cipher$$, 5, $$caesar_cipher("abc", 27)$$,          $$"bcd"$$,           TRUE),

  /* Anagram Check (draft problem) */
  ($$Anagram Check$$, 1, $$are_anagrams("listen", "silent")$$, $$TRUE$$,  FALSE),
  ($$Anagram Check$$, 2, $$are_anagrams("hello", "world")$$,   $$FALSE$$, TRUE)

) AS v(title, sort_order, code, expected_output, is_hidden)
JOIN problems p ON p.title = v.title;

COMMIT;

/* Quick sanity check */
SELECT t.name AS topic, p.sort_order, p.title, p.difficulty,
       COUNT(tc.id) AS test_cases,
       COUNT(tc.id) FILTER (WHERE NOT tc.is_hidden) AS visible
FROM topics t
LEFT JOIN problems p ON p.topic_id = t.id
LEFT JOIN test_cases tc ON tc.problem_id = p.id
GROUP BY t.name, t.sort_order, p.id, p.sort_order, p.title, p.difficulty
ORDER BY t.sort_order NULLS LAST, p.sort_order NULLS LAST;
