# Python Training - Rebuild Plan

A self-paced, three-tier Python training for corporate colleagues who are new to
Python. Delivered as Jupyter notebooks. Each notebook is self-contained and follows
the same shape:

1. What you'll learn (objectives)
2. Concept sections with short runnable examples
3. Practice (hands-on exercises)
4. Summary (recap bullets)
5. Practice Solutions (at the bottom, so they do not spoil the exercises)

## Tiers and notebooks

### 01-beginner
- 01_getting_started.ipynb - what Python is, Jupyter cells, comments, print(), reading errors
- 02_variables_and_types.ipynb - variables, int/float/str/bool, type(), isinstance(), conversion
- 03_numbers_and_math.ipynb - arithmetic and operators, multiple assignment, readable numbers
- 04_strings.ipynb - indexing, slicing, methods, f-strings, input()
- 05_making_decisions.ipynb - comparison/logical operators, if/elif/else, nested, chained
- 06_loops.ipynb - for, range, enumerate, while, break, continue

### 02-intermediate
- 01_lists.ipynb - list operations, slicing, nested lists, copy by reference vs value
- 02_dictionaries.ipynb - create/access/update/delete, loop keys/values/items
- 03_sets_and_tuples.ipynb - sets and tuples
- 04_comprehensions.ipynb - list and dictionary comprehensions
- 05_functions.ipynb - parameters, defaults, *args/**kwargs, return, scope, docstrings
- 06_modules_and_imports.ipynb - import, from-import, useful standard library (math, random, datetime)
- 07_files_and_errors.ipynb - reading/writing with `with`, try/except

### 03-advanced
- 01_classes.ipynb - classes, inheritance, super(), scope, overriding
- 02_numpy.ipynb - arrays, vectorized operations, indexing, aggregation
- 03_pandas_intro.ipynb - Series, DataFrame, create from dict/list/csv
- 04_pandas_selecting_editing.ipynb - loc/iloc, add/remove rows and columns, selection, slicing
- 05_pandas_analysis.ipynb - head/info/describe/value_counts/groupby/sort
- 06_data_cleaning_and_combining.ipynb - missing values, dtypes, merge/join, rename
- 07_visualizing_data.ipynb - quick charts with pandas .plot() and matplotlib basics
- 08_capstone_project.ipynb - small end-to-end analysis tying it together

## Supporting files
- README.md (root) - who it is for, setup, tier order, how to use
- requirements.txt - jupyterlab, numpy, pandas, matplotlib
- Per-stage README.md - objectives and order
- 02-intermediate/function_examples.py - recreated, referenced by the functions lesson
- 02-intermediate/data/Text_File.txt - recreated sample text file
- 03-advanced/data/populations.csv - recreated sample data (so the example code runs)

## Fixes carried out during the rebuild
- Bugs: df.append() -> pd.concat; the int(y) variable mismatch in type conversion;
  the "model a dog" docstring on the Vehicle class; use `with open(...)` for files.
- Terminology: replace the incorrect "imperative vs functional programming" framing
  with "repeating code vs using functions (the DRY idea)".
- Typos: full pass, including "thee should be error displayed" -> "there should be no error".
- Slides: all embedded slide images converted to markdown text plus runnable code,
  images dropped (notebooks shrink from ~4MB to small text files).
- Academic references removed: textbook reading lists, lecture/PyCharm references,
  chapter numbers, and stale version-pinned links. Keep at most one current
  official-docs link per topic where it genuinely helps.

## Build cadence
Build and commit one tier at a time, pausing after each so the notebooks can be
previewed in Jupyter before continuing: beginner -> intermediate -> advanced.

## Verification
Notebooks ship unexecuted (clean, no stale outputs) so learners run them fresh.
Before each commit, all lesson code is run outside the notebook to prove it works
(input()-based examples are checked with fixed test values). numpy/pandas/matplotlib
are installed before building the advanced tier so those notebooks can be executed.
