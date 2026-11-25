/*
  Rnold sample data: users and submissions

  Run with:
    psql -v ON_ERROR_STOP=1 -d <your_database> -f seed_rnold.sql

  Notes
  * Topics, problems and evaluation cases are not seeded here. The application
    loads them at startup, so start it once before running this script. A check
    at the top of the transaction stops the script with a clear message if a
    problem referenced below is missing.
  * Submissions reference problems by title, so no problem ids are hardcoded.
    The one exception is submissions.user_id, which uses the sample users'
    github_id.
  * users.github_id is the primary key and normally comes from GitHub. The
    sample users use negative ids, which GitHub never issues, so a real account
    signing in through OAuth can never match a sample row and inherit its role.
  * users.role follows the Role IntEnum: 1 = USER, 2 = ADMIN. The model's default
    is applied by Python and not by the database, so raw SQL must always set it.
  * created_at and last_login have server defaults, but explicit values are used
    so the sample data has a spread of dates. last_login is never earlier than
    created_at. Sample emails use example.com, which is reserved for documentation.
  * submissions.accepted is a boolean: TRUE means the attempt passed every
    evaluation case, FALSE means it did not. created_at has a server default, but
    explicit values are used so each user has a believable attempt history. A
    submission is never dated before its user's created_at or after their last_login.
  * Safe to run more than once. The script first deletes the sample users
    (github_id < 0), and their submissions go with them because
    submissions.user_id is ON DELETE CASCADE. Real users are never touched.
    To remove the sample data without reseeding:
      DELETE FROM users WHERE github_id < 0;
*/

BEGIN;

/* ------------------------------------------------------------------ */
/* Precondition: the problems used below must already be loaded        */
/* ------------------------------------------------------------------ */

DO $check$
DECLARE
  missing text;
BEGIN
  SELECT string_agg(t.title, ', ') INTO missing
  FROM unnest(ARRAY[
    'Sum of 3 Numbers',
    'Subtract Two Numbers',
    'Multiply Two Numbers',
    'Divide Two Numbers',
    'Powers of Two',
    'Concatenation',
    'Sum of Lengths',
    'Passive Aggressive'
  ]) AS t(title)
  WHERE NOT EXISTS (SELECT 1 FROM problems p WHERE p.title = t.title);

  IF missing IS NOT NULL THEN
    RAISE EXCEPTION 'Problems not found: %. Start the application once so it loads topics and problems, then rerun this script.', missing;
  END IF;
END
$check$;

/* ------------------------------------------------------------------ */
/* Reset: remove previous sample users (and their submissions)         */
/* ------------------------------------------------------------------ */

DELETE FROM users WHERE github_id < 0;

/* ------------------------------------------------------------------ */
/* Users: 2 admins and 3 regular users                                 */
/* ------------------------------------------------------------------ */

/* role: 1 = USER, 2 = ADMIN (the Role IntEnum) */
INSERT INTO users (github_id, github_email, username, role, created_at, last_login) VALUES
  (-1, $$rnoldadmin@example.com$$, $$rnoldadmin$$, 2, now() - interval '180 days', now() - interval '1 hour'),
  (-2, $$tidytess@example.com$$, $$tidytess$$, 2, now() - interval '150 days', now() - interval '2 days'),
  (-3, $$vectorvic@example.com$$, $$vectorvic$$, 1, now() - interval '120 days', now() - interval '3 hours'),
  /* Edge case: last active 10 days ago, so every submission predates that */
  (-4, $$pipedream@example.com$$, $$pipedream$$, 1, now() - interval '100 days', now() - interval '10 days'),
  (-5, $$factorfran@example.com$$, $$factorfran$$, 1, now() - interval '75 days', now() - interval '36 hours');

/* ------------------------------------------------------------------ */
/* Submissions                                                         */
/* accepted: TRUE = passed, FALSE = failed                             */
/* Covers: failed attempts followed by a pass, a problem resubmitted   */
/* after it was already solved, a problem attempted but never solved,  */
/* and a user who mostly passes on the first try.                      */
/* ------------------------------------------------------------------ */

INSERT INTO submissions (user_id, problem_id, accepted, created_at)
SELECT v.user_id, p.id, v.accepted, v.created_at
FROM (VALUES

  /* rnoldadmin: smoke tests of the first problems */
  (-1, $$Sum of 3 Numbers$$, TRUE, now() - interval '170 days'),
  (-1, $$Subtract Two Numbers$$, TRUE, now() - interval '169 days 23 hours'),
  (-1, $$Concatenation$$, FALSE, now() - interval '169 days'),
  (-1, $$Concatenation$$, TRUE, now() - interval '168 days 23 hours'),

  /* tidytess */
  (-2, $$Sum of 3 Numbers$$, TRUE, now() - interval '140 days'),
  (-2, $$Divide Two Numbers$$, FALSE, now() - interval '139 days'),
  (-2, $$Divide Two Numbers$$, TRUE, now() - interval '138 days 22 hours'),
  /* Edge case: attempted but never solved */
  (-2, $$Powers of Two$$, FALSE, now() - interval '120 days'),
  (-2, $$Passive Aggressive$$, TRUE, now() - interval '60 days'),

  /* vectorvic: the most active user */
  (-3, $$Sum of 3 Numbers$$, TRUE, now() - interval '110 days'),
  (-3, $$Multiply Two Numbers$$, FALSE, now() - interval '100 days'),
  (-3, $$Multiply Two Numbers$$, TRUE, now() - interval '99 days 23 hours'),
  (-3, $$Concatenation$$, TRUE, now() - interval '95 days'),
  /* Edge case: resubmitting a problem that was already solved */
  (-3, $$Concatenation$$, TRUE, now() - interval '94 days'),
  (-3, $$Powers of Two$$, FALSE, now() - interval '80 days'),
  (-3, $$Powers of Two$$, FALSE, now() - interval '79 days 23 hours'),
  (-3, $$Powers of Two$$, TRUE, now() - interval '79 days 20 hours'),
  (-3, $$Sum of Lengths$$, TRUE, now() - interval '2 days'),

  /* pipedream: three attempts at the first problem */
  (-4, $$Sum of 3 Numbers$$, FALSE, now() - interval '90 days'),
  (-4, $$Sum of 3 Numbers$$, FALSE, now() - interval '89 days 23 hours 40 minutes'),
  (-4, $$Sum of 3 Numbers$$, TRUE, now() - interval '89 days 23 hours'),
  (-4, $$Subtract Two Numbers$$, FALSE, now() - interval '70 days'),
  (-4, $$Subtract Two Numbers$$, TRUE, now() - interval '69 days 22 hours'),
  /* Edge case: attempted but never solved */
  (-4, $$Passive Aggressive$$, FALSE, now() - interval '20 days'),

  /* factorfran */
  (-5, $$Sum of 3 Numbers$$, TRUE, now() - interval '70 days'),
  (-5, $$Divide Two Numbers$$, FALSE, now() - interval '40 days'),
  (-5, $$Divide Two Numbers$$, TRUE, now() - interval '39 days 23 hours'),
  /* Edge case: attempted but never solved */
  (-5, $$Concatenation$$, FALSE, now() - interval '30 days'),
  (-5, $$Sum of Lengths$$, TRUE, now() - interval '5 days')

) AS v(user_id, title, accepted, created_at)
JOIN problems p ON p.title = v.title
ORDER BY v.created_at;

COMMIT;

/* Quick sanity check: users by role */
SELECT role, COUNT(*) AS users FROM users WHERE github_id < 0 GROUP BY role ORDER BY role;

/* Submissions per sample user, split by outcome */
SELECT u.username, u.role,
       COUNT(s.id) AS submissions,
       COUNT(s.id) FILTER (WHERE s.accepted) AS accepted,
       COUNT(s.id) FILTER (WHERE NOT s.accepted) AS not_accepted
FROM users u
LEFT JOIN submissions s ON s.user_id = u.github_id
WHERE u.github_id < 0
GROUP BY u.github_id, u.username, u.role
ORDER BY u.github_id DESC;
