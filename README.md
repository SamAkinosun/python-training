# Python Training

A self-paced introduction to Python, built for colleagues who are new to programming.
The material runs entirely in Jupyter notebooks, so you read, edit, and run real code
as you learn.

## Who this is for

People with little or no Python experience who want to get productive with Python and,
by the end, work with data using NumPy and pandas. No prior programming background is
assumed.

## How it is organised

The course is split into three stages. Work through them in order.

| Stage | Folder | What you cover |
|-------|--------|----------------|
| Beginner | `01-beginner` | The basics: variables, types, numbers, strings, decisions, loops |
| Intermediate | `02-intermediate` | Collections, comprehensions, functions, modules, files and errors |
| Advanced | `03-advanced` | Classes, NumPy, pandas, data cleaning, charts, a capstone project |
| Data Science | `04-data-science` | The analyst workflow applied to financial data: returns, risk, portfolios |
| Data Automation | `05-data-automation` | Command-line scripts and a scheduled pipeline (med-tech data, synthetic) |

Inside each folder, the notebooks are numbered. Start at `01_` and go up. Each stage has
its own `README.md` with the lesson list and learning objectives.

Every notebook is self-contained and follows the same shape:

1. What you'll learn
2. Worked examples you can run and change
3. Practice exercises
4. A short summary
5. Solutions to the practice exercises (at the very bottom)

## Setup

1. Install Python 3.10 or newer (the Anaconda distribution is an easy option, as it
   includes Jupyter and the data libraries).
2. From this folder, install the requirements:

   ```
   pip install -r requirements.txt
   ```

   If you use conda instead:

   ```
   conda install jupyterlab numpy pandas matplotlib
   ```

3. Launch JupyterLab:

   ```
   jupyter lab
   ```

4. In the browser tab that opens, open `index.ipynb` for a clickable map of every lesson,
   then start with `01-beginner/01_getting_started.ipynb`.

## How to use a notebook

Click a code cell and press **Shift+Enter** to run it and move to the next cell. Change
the code and run it again to see what happens. Breaking things on purpose is one of the
fastest ways to learn.
