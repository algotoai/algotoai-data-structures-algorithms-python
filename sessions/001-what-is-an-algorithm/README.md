# Session 001 · What Makes an Algorithm?

**Video:** Coming soon
**Course:** [Data Structures & Algorithms with Python](../../README.md)

## Start Here: 3 Simple Steps

1. Read the example in [section 4](#4-the-python-code) and run [`example.py`](example.py).
2. Change the numbers, predict the result, and run the program again.
3. Complete [`starter.py`](starter.py) and [check your answer](exercises.md#check-your-work).

The rest of this page explains each step.

## 1. What Will You Learn?

In this session you will:

- learn what an **algorithm** is
- follow one algorithm step by step: finding the **largest number in a list**
- read the Python code for it, line by line
- predict what the program prints, then change the numbers and run it again

You only need to know variables, lists, `for` loops, `if` statements, `print()` and comparisons such as `>`.

## 2. The Problem

Here is a list of numbers:

```text
3, 7, 2, 9, 5
```

Which one is the largest? You can see the answer, **9**, at a glance. But how did you find it?

A computer cannot "see" the answer. It needs **exact steps** to follow. If the list had a million numbers, you would need exact steps too.

An **algorithm** is a set of clear steps that solves a problem. A good algorithm:

- starts from some **input** (here: a list of numbers)
- has steps that are **clear**, so anyone following them does the same thing
- always **finishes**
- gives an **output** (here: the largest number)

## 3. Let's Solve It Step by Step

Here is the algorithm in plain English:

1. Remember the **first number** as "the largest so far".
2. Look at each number in the list, one at a time.
3. If the number is **bigger** than the largest so far, remember it as the new largest so far.
4. When you have looked at every number, the largest so far is the answer.

Let's follow it with `3, 7, 2, 9, 5`. We start with **largest = 3**.

| Number we look at | Is it bigger than the largest so far? | Largest so far |
|---|---|---|
| 3 | 3 > 3? No | 3 |
| 7 | 7 > 3? **Yes** | **7** |
| 2 | 2 > 7? No | 7 |
| 9 | 9 > 7? **Yes** | **9** |
| 5 | 5 > 9? No | 9 |

The largest so far changed **twice**: to 7, then to 9. After the last number, the answer is **9**.

Following an algorithm by hand like this, one row per step, is called **tracing**. It is the best way to understand what an algorithm really does.

## 4. The Python Code

The same steps in Python ([`example.py`](example.py)):

```python
numbers = [3, 7, 2, 9, 5]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

What each line does:

| Line | Meaning |
|---|---|
| `numbers = [3, 7, 2, 9, 5]` | The input: the list we want to search. |
| `largest = numbers[0]` | Step 1: remember the first number (position 0) as the largest so far. |
| `for number in numbers:` | Step 2: look at each number in the list, one at a time. |
| `if number > largest:` | Step 3: is this number bigger than the largest so far? |
| `largest = number` | If yes, it becomes the new largest so far. |
| `print(largest)` | Step 4: show the answer. |

The loop also looks at the first number, so the first check is `3 > 3`. That is `False`, so nothing changes. This is harmless and keeps the code simple.

## 5. Understanding the Output

Run the program from this folder:

```bash
python example.py
```

(On some computers, especially macOS, the command is `python3` instead of `python`.)

It prints:

```text
9
```

Two things to notice:

- **Negative numbers work.** For `[-8, -3, -11]` the program prints `-3`. That's because we start from a number that is really in the list, not from `0`. If we started from `0`, the answer would be `0`, which is not even in the list!
- **Repeated numbers work.** For `[4, 9, 2, 9]` the program prints `9`. When the second `9` arrives, `9 > 9` is `False`, so the largest so far simply stays `9`.

**One rule for this lesson:** the list must contain **at least one number**. The first step reads `numbers[0]`, and an empty list has no first number, so Python would stop with an error. Handling an empty list is something we will come back to in a later session.

## 6. Try It Yourself

Open `example.py`, change the list, and run it again. **Before each run, predict the answer.**

- `[10, 4, 6]`: the largest number comes first
- `[1, 2, 3, 4]`: the largest number comes last
- `[-5, -1, -9]`: all negative
- `[6, 6, 6]`: all the same
- `[42]`: just one number

Was your prediction right every time? If not, trace the list by hand with a table like the one in section 3.

## 7. Exam Practice

You should be able to:

- trace the algorithm by hand with a table
- say exactly when the largest so far changes
- predict the final result

Questions with answers are in [`exercises.md`](exercises.md#part-a-exam-practice).

## 8. Coding Practice

Your first step toward writing real programs:

- complete [`starter.py`](starter.py) so it prints the largest number
- change the input list and run it again
- check the result yourself, and with the provided checker
- try negative numbers and repeated numbers

Instructions are in [`exercises.md`](exercises.md#part-b-coding-practice).

## 9. What Comes Next?

You have written your first algorithm and traced it by hand.

In the next session, *Big-O Notation: Intuition and Basic Examples*, we ask a new question: **how much work** does an algorithm do when the list gets longer?

Later sessions return to this example to handle an empty list and to turn it into a reusable function.
