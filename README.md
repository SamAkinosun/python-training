# Python Training

A self-paced introduction to Python, built for colleagues who are new to programming.
The material runs entirely in Jupyter notebooks, so you read, edit, and run real code
as you learn.

## Who this is for

People with little or no Python experience who want to get productive with Python and,
by the end, work with data using NumPy and pandas, build AI agents, and train machine
learning models. No prior programming background is assumed.

## How it is organised

The course is split into seven stages. Work through them in order.

| Stage | Folder | Lessons | What you cover |
|-------|--------|---------|----------------|
| Beginner | `01-beginner` | 6 | The basics: variables, types, numbers, strings, decisions, loops |
| Intermediate | `02-intermediate` | 7 | Collections, comprehensions, functions, modules, files and errors |
| Advanced | `03-advanced` | 8 | Classes, NumPy, pandas, data cleaning, charts, a capstone project |
| Data Science | `04-data-science` | 10 | The analyst workflow applied to financial data: returns, risk, portfolios |
| Data Automation | `05-data-automation` | 6 | Automation notebooks and a scheduled pipeline (med-tech data, synthetic) |
| AI Agents | `06-ai-agents` | 8 | Build an AI agent with Claude or ChatGPT: tools, the agent loop, memory, guardrails (FP&A data, synthetic) |
| Machine Learning | `07-machine-learning` | 10 | scikit-learn, PyTorch, and TensorFlow: regression, classification, clustering, neural networks |

Inside each folder, the notebooks are numbered. Start at `01_` and go up. Each stage has
its own `README.md` with the lesson list and learning objectives.

Every lesson notebook is self-contained (it loads its own data and sets up what it
needs, so you can open any lesson directly) and follows the same shape:

1. What you'll learn
2. Worked examples you can run and change
3. Practice exercises
4. A short summary
5. Solutions to the practice exercises (at the very bottom)

Two kinds of notebook skip the exercises: the data generators (`generate_data.ipynb`,
`generate_sample_data.ipynb`), and the Stage 5 pipeline notebooks, which the pipeline runs
from start to finish.

## The data

Every dataset in this course is **synthetic**: made up with a fixed random seed, so it is
reproducible and contains no real company, customer, patient, or market data. Each stage
that uses data includes a generator notebook to recreate it.

## Libraries by stage

| Stages | Libraries |
|--------|-----------|
| 1 to 2 | Python only |
| 3 to 5 | NumPy, pandas, matplotlib |
| 6 | pandas, plus `anthropic` (Claude) or `openai` (ChatGPT) |
| 7 | pandas, scikit-learn, PyTorch (`torch`), TensorFlow (`tensorflow`) |

## Setup

1. Install Python 3.10 or newer (the Anaconda distribution is an easy option, as it
   includes Jupyter and the data libraries).
2. From this folder, install the requirements:

   ```
   pip install -r requirements.txt
   ```

   If you use conda, install the core libraries with conda and the rest with pip:

   ```
   conda install jupyterlab numpy pandas matplotlib scikit-learn
   pip install torch tensorflow anthropic openai
   ```

   Stage 6 also needs your own API key from Anthropic (Claude) or OpenAI (ChatGPT);
   `06-ai-agents/02_api_key_and_first_call.ipynb` shows how to set it up. Keep your key
   in an environment variable, never in a notebook, and never commit it to git.

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
