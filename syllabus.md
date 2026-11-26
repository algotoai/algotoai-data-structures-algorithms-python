# Syllabus: Data Structures & Algorithms with Python

**Status: proposed.** This is the intended order of the first twelve sessions. Titles, order and scope may change as lessons are developed.
Only [Session 001](sessions/001-what-is-an-algorithm/) is available so far.

Each session is a short video lesson (about 2–4 minutes) plus a session folder with a worked example, Exam Practice, Coding Practice and tests.
Every session follows the same teaching sequence:

> **Problem → visual intuition → step-by-step trace → Python code → complexity and pitfalls → practice**

## Part 1 · Foundations

| # | Session | Exam Ready | Job Ready | Builds on |
|---|---|---|---|---|
| 001 | **What Makes an Algorithm?** | Describe an algorithm as clear steps; trace "find the largest number" by hand; say when the largest so far changes; predict the result | Write the loop yourself; change the input and run it again; check negative numbers and duplicates (non-empty lists only) | Basic Python: variables, lists, `for`, `if`, `print` |
| 002 | **Big-O Notation: Intuition and Basic Examples** | Count steps; state O(1), O(n), O(n²), O(log n) for simple loops; best vs worst case | Estimate how code scales; spot accidental quadratic loops | 001 |
| 003 | **Arrays vs Python Lists: Concepts and Trade-offs** | Contiguous storage, indexing cost, insertion/deletion cost, dynamic arrays | Choose list operations by cost (`append` vs `insert(0, x)`); measure with `timeit` | 002 |

## Part 2 · Sorting basics

| # | Session | Exam Ready | Job Ready | Builds on |
|---|---|---|---|---|
| 004 | **Selection Sort: Visual Trace and Python Implementation** | Trace passes; invariant (sorted prefix); O(n²) comparisons; not stable | Implement and test in place; edge cases (empty, one element, duplicates) | 001–003 |
| 005 | **Bubble Sort: Visual Trace and Python Implementation** | Trace swaps; early-exit optimisation; best/worst case; stability | Implement with early exit; test stability with records | 004 |
| 006 | **Insertion Sort: Visual Trace and Python Implementation** | Trace shifts; invariant; O(n) best case on nearly sorted input | Implement; know when it beats the others (small or nearly sorted data) | 004–005 |

## Part 3 · Searching

| # | Session | Exam Ready | Job Ready | Builds on |
|---|---|---|---|---|
| 007 | **Linear Search vs Binary Search** | Sorted-input precondition; trace `low`/`mid`/`high`; O(n) vs O(log n) | Implement binary search without off-by-one errors; not found, duplicates, empty input; `bisect` | 002, 004–006 |

## Part 4 · Core data structures

| # | Session | Exam Ready | Job Ready | Builds on |
|---|---|---|---|---|
| 008 | **Stack and LIFO** | Push/pop/peek semantics and costs; trace bracket matching | Implement a stack on a list; solve balanced brackets; handle popping an empty stack | 003 |
| 009 | **Queue and FIFO** | Enqueue/dequeue; why `list.pop(0)` is O(n); circular buffer idea | Use `collections.deque`; implement a queue; simulate a task queue | 003, 008 |
| 010 | **Linked Lists: Nodes and Pointers** | Node structure; insert/delete by pointer updates; costs vs arrays | Implement a singly linked list; traverse, insert and delete; edge cases at head and tail | 003 |

## Part 5 · Recursion and divide and conquer

| # | Session | Exam Ready | Job Ready | Builds on |
|---|---|---|---|---|
| 011 | **Recursion: Base Case and Call Stack** | Base case and recursive case; trace the call stack; recursion depth | Write recursive functions safely; recursion vs iteration; Python's recursion limit | 008 |
| 012 | **Merge Sort: Divide and Conquer** | Divide, conquer, combine; trace merges; O(n log n); stability; extra space | Implement merge and merge sort; test against `sorted`; compare with insertion sort | 004–007, 011 |

## Later (proposed, not yet scheduled)

Hash tables · trees and binary search trees · heaps and priority queues · graphs and graph traversal (BFS/DFS) · greedy algorithms · dynamic programming · interview problem patterns

## Assessment in every session

- **Exam Practice:** definitions, traces, correctness arguments, complexity questions (answers included, folded).
- **Coding Practice:** code to complete in `starter.py`, checked by `tests/test_exercises.py`. Reference solutions are in `solutions/`.
