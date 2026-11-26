# Session 001 · Exercises

Read the [session README](README.md) first. Try each question before you open its answer.

---

## Part A: Exam Practice

**Goal (Exam Ready):** trace the algorithm by hand, say when the largest so far changes, and predict the final result.
Use paper and a pencil. No computer needed.

### Core exercises

Start with these two. They are the most important.

**A1.** Write the four steps of the algorithm in your own words.

**A2.** Trace the algorithm for `[4, 1, 8, 8, 3]`. Make a table with one row per number.
How many times does the largest so far change? What does the program print?

### Optional practice

More tracing and reasoning, if you want extra practice.

**A3.** Trace the algorithm for `[-6, -2, -9]`. What does the program print?

**A4.** For each list, how many times does the largest so far change after the start?
1. `[5, 5, 5]`
2. `[1, 2, 3, 4]`
3. `[4, 3, 2, 1]`

**A5.** A student starts with `largest = 0` instead of `largest = numbers[0]`.
Find a list where the student's program prints the wrong answer. What does it print, and what should it print?

**A6.** In `example.py`, the `>` in `if number > largest:` is changed to `<`.
What does the program print for `[3, 7, 2, 9, 5]`? What does the changed program find?

<details>
<summary>Answers to Part A</summary>

**A1.** For example:
1. Remember the first number as the largest so far.
2. Look at each number in turn.
3. If it is bigger than the largest so far, remember it instead.
4. At the end, the largest so far is the answer.

**A2.** Start: largest = 4.

| Number | Bigger than the largest so far? | Largest so far |
|---|---|---|
| 4 | 4 > 4? No | 4 |
| 1 | 1 > 4? No | 4 |
| 8 | 8 > 4? **Yes** | **8** |
| 8 | 8 > 8? No | 8 |
| 3 | 3 > 8? No | 8 |

It changes **once** (to 8). The program prints `8`.

**A3.** Start: largest = −6. Then −6 > −6? No. −2 > −6? **Yes**, so largest = −2. −9 > −2? No. The program prints `-2`.

**A4.**
1. `[5, 5, 5]`: **0** times. `5 > 5` is never true.
2. `[1, 2, 3, 4]`: **3** times (to 2, 3 and 4). Every number is bigger than the one before.
3. `[4, 3, 2, 1]`: **0** times. The first number is already the largest.

**A5.** Any list where every number is negative, for example `[-6, -2, -9]`. The student's program prints `0`, but the answer is `-2`. The number `0` is not even in the list. Starting from `numbers[0]` avoids this, because the starting value always comes from the list.

**A6.** It prints `2`. With `<`, the program remembers a number when it is *smaller*, so it finds the **smallest** number.
</details>

---

## Part B: Coding Practice

**Goal (Job Ready, first step):** change the input, run the program, check the result, and try negative and repeated numbers.
This is a first step. Writing professional, tested software comes later in the course.

### Main exercise

Open [`starter.py`](starter.py):

```python
numbers = [12, -4, 25, 25, 8]

largest = numbers[0]

# Write your loop here.

print(largest)
```

Replace the comment with a loop so that the program prints the **largest number** in `numbers`.

1. Run it from this folder: `python starter.py`
2. It should print `25`. Right now it prints `12`, because the loop is missing.
3. Change the list and run it again. Predict the answer each time. Try:
   - only negative numbers, such as `[-7, -3, -10]` (expected: `-3`)
   - repeated numbers, such as `[2, 9, 9, 1]` (expected: `9`)
   - one number, such as `[5]` (expected: `5`)

Keep at least one number in the list. This lesson does not handle an empty list.

### Check your work

From this session's folder (the same place you ran `starter.py`), run:

```bash
python tests/test_exercises.py
```

The checker runs your `starter.py` with several different lists and tells you which ones give the right answer. You do not need to read or change the checker.

When everything passes, compare your code with [`solutions/solution.py`](solutions/solution.py).

### Optional variations

Do these in a **new file** (for example `my_variation.py`), so `starter.py` stays as the checker expects.

**Variation 1: Watch it change.** Print a message every time the largest so far changes, such as `New largest: 25`. How many messages do you expect for `[12, -4, 25, 25, 8]`?

**Variation 2: The smallest number.** Find the smallest number instead. Use a variable called `smallest`, and think about which comparison you need. (Exam question A6 gives a hint.)
