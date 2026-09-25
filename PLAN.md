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

### 04-data-science (added after the initial three tiers)
Applied analyst workflow using synthetic financial data (offline, reproducible).
- 01_data_science_workflow.ipynb - the workflow and toolkit
- 02_loading_and_inspecting.ipynb - inspect size, types, gaps; slice a time series
- 03_cleaning_and_preparing.ipynb - duplicates and missing values
- 04_exploring_and_aggregating.ipynb - groupby, pivot_table, resample
- 05_financial_returns.ipynb - daily, cumulative, and log returns
- 06_moving_averages_and_trends.ipynb - rolling averages and trend signals
- 07_volatility_and_risk.ipynb - volatility, annualising, drawdown
- 08_portfolio_analysis.ipynb - weights, correlation, portfolio returns
- 09_visualizing_financial_data.ipynb - rebased lines, histograms, heatmaps
- 10_capstone_portfolio_report.ipynb - end-to-end report
- generate_data.ipynb + data/stock_history.csv - reproducible synthetic OHLCV data

### 05-data-automation (added after the data science stage)
Simple single-purpose notebooks forming a med-tech data pipeline (synthetic data, no real PHI).
- generate_sample_data.ipynb - synthetic daily device-reading CSVs with deliberate blemishes
- 01_combine_csvs.ipynb - stack daily files into one
- 02_validate_readings.ipynb - flag missing and out-of-range values into a report
- 03_clean_and_standardize.ipynb - dedupe, standardise clinic names/types, convert F to C
- 04_daily_summary_report.ipynb - summarise by day, clinic, metric
- 05_archive_files.ipynb - move processed inputs into a dated archive
- run_pipeline.ipynb - run all steps in order (schedulable via cron / Task Scheduler)
- Generated data lives under data/ and is gitignored.

### Script to notebook conversion (done 2026-09-25)
Every .py file becomes an .ipynb so the whole course opens in Jupyter. The .py originals
are removed.
- 02-intermediate/function_examples.py -> function_examples.ipynb
- 04-data-science/generate_data.py -> generate_data.ipynb
- 05-data-automation: generate_sample_data, 01-05 steps and run_pipeline all become
  notebooks. Each step notebook still runs on its own, in order. run_pipeline.ipynb runs
  each step in a fresh kernel with nbclient (ships with Jupyter) and stops at the first
  failing step. A scheduler runs it with
  `jupyter nbconvert --to notebook --execute --output-dir data/logs run_pipeline.ipynb`.
- Paths use os.getcwd() instead of __file__ (which does not exist in a notebook); Jupyter
  and nbconvert both run a notebook from its own folder.
- Proof it did not break: every notebook passes nbformat validation (opens in JupyterLab),
  runs top to bottom with nbconvert, and the 05 outputs match what the old scripts wrote.
- READMEs, index.ipynb and this plan are updated to the new file names.

### 06-ai-agents (added 2026-09-25)
Building an AI agent in Python with synthetic FP&A data. Same shape as 04: one committed
dataset, every notebook loads it and sets itself up in its first cells, so any lesson runs
on its own.
- data/fpa_actuals_budget.csv - 2023-01 to 2025-12, monthly, by ProductLine and Region:
  Revenue, Budget_Revenue, COGS, Budget_COGS, OpEx, Budget_OpEx, Headcount, FX_Rate (USD
  thousands). Fictional company, fixed seed, five deliberate events for the agent to find
  (listed in generate_data.ipynb as the answer key).
- generate_data.ipynb - recreates the dataset
- 01_what_is_an_ai_agent.ipynb - model vs workflow vs agent; variance by hand with pandas
- 02_api_key_and_first_call.ipynb - getting a key, setting it safely, first call, errors
- 03_prompts_and_structured_output.ipynb - system prompts, JSON schema output
- 04_giving_the_model_tools.ipynb - pandas functions as tools, one round trip by hand
- 05_the_agent_loop.ipynb - the loop with a step limit and a trace
- 06_memory_and_conversation.ipynb - conversation history and follow-up questions
- 07_guardrails_and_checking.ipynb - validation, audit log, number check, human review flag
- 08_capstone_fpa_analyst_agent.ipynb - variance commentary agent ("# Your code" + solution)
Providers: each notebook starts with `PROVIDER = "anthropic"` or `"openai"` (models
claude-opus-5 and gpt-5.6). Helpers show both code paths: Anthropic Messages API
(`client.messages.create`, `tool_use` / `tool_result` blocks, `output_config` JSON schema)
and OpenAI Responses API (`client.responses.create`, `function_call` /
`function_call_output` items, `text.format` JSON schema).
API keys: no key is stored anywhere in the repo. Trainees add their own Claude or OpenAI
key as ANTHROPIC_API_KEY / OPENAI_API_KEY before starting Jupyter, or through a getpass
prompt kept in memory only. Without a key the pandas parts run and model cells print
"(Skipped: no API key ...)".

### 07-machine-learning (added 2026-09-25)
Simple machine learning with scikit-learn, PyTorch, and TensorFlow (Keras), using
synthetic customer-account data.
- data/customer_accounts.csv - 2,000 fictional accounts; regression target
  next_year_spend, classification target paid_late, behaviour columns for clustering, and
  a few blemishes (missing values, lower-case regions)
- generate_data.ipynb - recreates the dataset
- 01_what_is_machine_learning.ipynb - features, targets, train/test split, baseline
- 02_linear_regression.ipynb - coefficients, MAE/RMSE/R2, one-hot encoding
- 03_classification_logistic_regression.ipynb - probabilities, accuracy trap, threshold
- 04_decision_trees_and_random_forests.ipynb - rules, overfitting, feature importance
- 05_evaluating_models.ipynb - confusion matrix, precision/recall, ROC AUC, cross-validation
- 06_preprocessing_and_pipelines.ipynb - imputer, encoder, scaler, ColumnTransformer,
  Pipeline, GridSearchCV, joblib save/load
- 07_clustering_kmeans.ipynb - scaling, elbow, silhouette, cluster profiles
- 08_neural_networks_with_pytorch.ipynb - tensors, autograd, nn.Sequential, training loop
- 09_neural_networks_with_tensorflow.ipynb - keras.Sequential, compile/fit, early stopping
- 10_capstone_ml_project.ipynb - compare models, risk list, save model
Saved models go to 07-machine-learning/models/ (gitignored).

requirements.txt gains scikit-learn, torch, tensorflow, anthropic and openai.

## Supporting files
- README.md (root) - who it is for, setup, tier order, how to use
- requirements.txt - jupyterlab, numpy, pandas, matplotlib, scikit-learn, torch,
  tensorflow, anthropic, openai
- Per-stage README.md - objectives and order
- 02-intermediate/function_examples.ipynb - recreated, referenced by the functions lesson
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
Stages 6 and 7 were built together in one pass on request, then reviewed as a whole.

## Verification
Notebooks ship unexecuted (clean, no stale outputs) so learners run them fresh.
Before each commit, all lesson code is run outside the notebook to prove it works
(input()-based examples are checked with fixed test values). numpy/pandas/matplotlib
are installed before building the advanced tier so those notebooks can be executed.
Stage 6 model calls are verified without any real API key: every notebook is executed
through the real anthropic and openai SDKs against a local stand-in server (both
providers), and again with no key set.
