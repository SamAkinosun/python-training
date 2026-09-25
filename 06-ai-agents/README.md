# Stage 6: AI Agents

How to build an AI agent in Python: a large language model (Claude or ChatGPT) that
answers business questions by calling Python functions you write. The worked example is
an FP&A analyst agent that explains budget variances.

Make sure the libraries are installed (from the project root):

```
pip install -r requirements.txt
```

## You need an API key

Lessons 2 to 8 call a model, so you need your own API key from **Anthropic (Claude)** or
**OpenAI (ChatGPT)**. Lesson 2 shows where to get one and how to set it safely. Every
lesson starts with the same setup cell; change `PROVIDER = "anthropic"` to
`PROVIDER = "openai"` if you use ChatGPT. Without a key, the pandas parts still run and
the model cells print a short "skipped" message.

API calls are billed by the provider per request. The lessons use small requests.

## The dataset

`data/fpa_actuals_budget.csv` is **synthetic**: three years (2023-01 to 2025-12) of monthly
actuals and budget for a fictional company, by product line and region, in USD thousands.
It is produced by `generate_data.ipynb` with a fixed random seed and contains no real
company, customer, or employee data. Only synthetic data is sent to the model in these
lessons; follow your organisation's rules before sending real data to any provider.

## Lessons

| # | Notebook | You will be able to |
|---|----------|---------------------|
| 1 | `01_what_is_an_ai_agent.ipynb` | Explain models, workflows, and agents; answer a variance question with pandas |
| 2 | `02_api_key_and_first_call.ipynb` | Set up an API key safely and make your first model call |
| 3 | `03_prompts_and_structured_output.ipynb` | Write system prompts and get JSON that matches a schema |
| 4 | `04_giving_the_model_tools.ipynb` | Turn Python functions into tools and handle one tool call |
| 5 | `05_the_agent_loop.ipynb` | Build the agent loop with a step limit |
| 6 | `06_memory_and_conversation.ipynb` | Give an agent memory for follow-up questions |
| 7 | `07_guardrails_and_checking.ipynb` | Validate inputs, log tool calls, and check the agent's numbers |
| 8 | `08_capstone_fpa_analyst_agent.ipynb` | Build a variance-commentary agent end to end |

## Files in this folder

- `generate_data.ipynb` - regenerates the synthetic dataset.
- `data/fpa_actuals_budget.csv` - the generated data used by every lesson.

## How to work through a notebook

Every notebook runs on its own: it loads the data and sets up everything it needs in its
first cells. Read each section, run the cells, and do the **Practice** before checking the
**Practice Solutions** at the bottom.
