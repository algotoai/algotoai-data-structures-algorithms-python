# Data Structures & Algorithms with Python

**An [Algo to AI](https://www.youtube.com/@Algo-to-AI) course · Learn CS Visually**

Learn Data Structures and Algorithms with Python through visual explanations, university-style exercises, coding challenges, and practical implementations.

## Purpose

This course takes you from "what is an algorithm?" to the core data structures and algorithms of a Computer Science degree. Each lesson is a short video plus a session folder in this repository with runnable code, exercises and tests.

Every session works toward two goals:

| | You will be able to… |
|---|---|
| **Exam Ready** | explain the concept precisely, trace it by hand, reason about correctness and complexity, and answer university-style questions |
| **Job Ready** | implement it in Python, handle edge cases, test it, explain trade-offs, and solve interview-style problems |

Watching alone is not enough: the exercises and tests are where the learning happens.

## Who it is for

- Computer Science and Computer Engineering students taking (or preparing for) a Data Structures & Algorithms course
- Self-taught programmers and early-career developers strengthening their foundations or preparing for technical interviews

## Prerequisites

- **Python 3.10 or newer** installed, and able to run a file: `python example.py`
- Reading basic Python: variables, lists, `for` loops, `if` statements, `print()` and comparisons. Later sessions introduce functions.
- No prior Data Structures & Algorithms knowledge is assumed

The course does not teach basic Python syntax. If loops and functions are new to you, learn those first, then come back.

## How to use this repository

Each lesson lives in its own folder under [`sessions/`](sessions/):

```text
sessions/NNN-topic/
├── README.md              # the lesson: objectives, explanation, outcomes, video link
├── example.py             # the documented worked example
├── exercises.md           # Exam Practice (on paper) + Coding Practice
├── starter.py             # your code goes here
├── tests/test_exercises.py # a checker for your starter.py (you don't need to read it)
└── solutions/solution.py  # reference solution: try first!
```

Suggested routine for every session:

1. Watch the video (when it is published) and read the session `README.md`.
2. Run `example.py` and change it to see what happens.
3. Answer the **Exam Practice** questions on paper.
4. Complete `starter.py` until the checker passes.
5. Only then compare with `solutions/solution.py`.

Check your work from the repository root (plain Python, nothing to install):

```bash
python sessions/001-what-is-an-algorithm/tests/test_exercises.py
```

## How sessions are written

**Simple First, Advanced Later.** Each session starts from the simplest correct code a beginner can read. More advanced Python (functions, error handling, testing tools) is introduced only once a later session has explained it. See [`sessions/GUIDELINES.md`](sessions/GUIDELINES.md).

## Learning path

This course is the first in the Algo to AI path. The lessons build on each other: take them in order.

1. **Foundations:** algorithmic thinking, Big-O, arrays and lists
2. **Sorting basics:** selection, bubble and insertion sort
3. **Searching:** linear search and binary search
4. **Core data structures:** stacks, queues, linked lists
5. **Recursion and divide and conquer:** recursion, merge sort

Later topics (proposed): hash tables, trees, heaps, graphs and graph traversal, dynamic programming, interview problem patterns.
The full proposed sequence is in [`syllabus.md`](syllabus.md).

## Sessions

| # | Session | Video | Status |
|---|---|---|---|
| 001 | [What Makes an Algorithm?](sessions/001-what-is-an-algorithm/) | Coming soon | Available |
| 002 | Big-O Notation: Intuition and Basic Examples | — | Planned |
| 003 | Arrays vs Python Lists: Concepts and Trade-offs | — | Planned |
| 004 | Selection Sort: Visual Trace and Python Implementation | — | Planned |
| 005 | Bubble Sort: Visual Trace and Python Implementation | — | Planned |
| 006 | Insertion Sort: Visual Trace and Python Implementation | — | Planned |
| 007 | Linear Search vs Binary Search | — | Planned |
| 008 | Stack and LIFO | — | Planned |
| 009 | Queue and FIFO | — | Planned |
| 010 | Linked Lists: Nodes and Pointers | — | Planned |
| 011 | Recursion: Base Case and Call Stack | — | Planned |
| 012 | Merge Sort: Divide and Conquer | — | Planned |

Planned titles and their order may change as the course is developed.

## Channel

Videos are published on the **Algo to AI** YouTube channel: <https://www.youtube.com/@Algo-to-AI>.
