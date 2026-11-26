"""Checker for Session 001 - you do not need to read or change this file.

Run it from the session folder (or give the full path from anywhere):

    python tests/test_exercises.py            # checks starter.py
    python tests/test_exercises.py solution   # checks solutions/solution.py
    python tests/test_exercises.py example    # checks example.py

It runs the program several times, each time with a different list in the
`numbers = [...]` line, and compares the last number it prints with the
correct answer. Every list has at least one number, as the lesson requires.

Until you finish starter.py, some checks are expected to fail.
"""

import contextlib
import io
import pathlib
import sys

SESSION = pathlib.Path(__file__).resolve().parent.parent
PROGRAMS = {
    "starter": SESSION / "starter.py",
    "solution": SESSION / "solutions" / "solution.py",
    "example": SESSION / "example.py",
}

CASES = [
    ("a normal list", [3, 7, 2, 9, 5], 9),
    ("negative numbers", [-8, -3, -11, -5], -3),
    ("duplicate values", [4, 9, 2, 9, 1], 9),
    ("one number", [42], 42),
    ("largest number first", [9, 1, 2], 9),
    ("largest number last", [1, 2, 9], 9),
]


def run_with_list(program, numbers):
    """Run the program with its `numbers = ...` line replaced; return its last printed line."""
    lines = program.read_text().splitlines()
    positions = [i for i, line in enumerate(lines) if line.startswith("numbers = ")]
    if len(positions) != 1:
        return f"(the program needs exactly one line starting with 'numbers = ', found {len(positions)})"
    lines[positions[0]] = f"numbers = {numbers!r}"
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec("\n".join(lines), {"__name__": "__main__"})
    except Exception as error:
        return f"(an error: {type(error).__name__}: {error})"
    printed = output.getvalue().strip().splitlines()
    return printed[-1].strip() if printed else "(nothing was printed)"


def check(name):
    program = PROGRAMS[name]
    print(f"Checking {program.relative_to(SESSION)}\n")
    passed = 0
    for label, numbers, expected in CASES:
        got = run_with_list(program, numbers)
        if got == str(expected):
            passed += 1
            print(f"  PASS  {label}: {numbers} -> {got}")
        else:
            print(f"  FAIL  {label}: {numbers} -> expected {expected}, got {got}")
    print(f"\n{passed} of {len(CASES)} checks passed.")
    return passed == len(CASES)


# Repository checks for pytest. They check the finished programs only:
# starter.py is meant to be incomplete until a learner finishes it.
def test_solution():
    assert check("solution")


def test_example():
    assert check("example")


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "starter"
    if name not in PROGRAMS:
        sys.exit(f"Unknown program '{name}'. Use one of: {', '.join(PROGRAMS)}")
    sys.exit(0 if check(name) else 1)
