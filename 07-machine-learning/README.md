# Stage 7: Machine Learning

Simple machine learning in Python with the three libraries you will meet most often:
**scikit-learn** for classic models, and **PyTorch** and **TensorFlow (Keras)** for neural
networks. The worked example predicts customer spend and late payments, and groups
customers by buying behaviour.

Make sure the libraries are installed (from the project root):

```
pip install -r requirements.txt
```

## The dataset

`data/customer_accounts.csv` is **synthetic**: 2,000 fictional customer accounts with their
segment, region, order history, discounts, support tickets, payment behaviour, next-year
spend, and whether they paid late. It is produced by `generate_data.ipynb` with a fixed
random seed and contains no real customer data. A few missing values and inconsistent
region names are included on purpose for the preprocessing lesson.

## Lessons

| # | Notebook | You will be able to |
|---|----------|---------------------|
| 1 | `01_what_is_machine_learning.ipynb` | Explain supervised and unsupervised learning; split data; beat a baseline |
| 2 | `02_linear_regression.ipynb` | Predict a number and measure the error |
| 3 | `03_classification_logistic_regression.ipynb` | Predict a yes/no outcome and choose a threshold |
| 4 | `04_decision_trees_and_random_forests.ipynb` | Train trees and forests and read feature importance |
| 5 | `05_evaluating_models.ipynb` | Use the confusion matrix, precision, recall, ROC AUC, and cross-validation |
| 6 | `06_preprocessing_and_pipelines.ipynb` | Build a leak-free pipeline, tune it, and save it |
| 7 | `07_clustering_kmeans.ipynb` | Group customers with KMeans and describe the clusters |
| 8 | `08_neural_networks_with_pytorch.ipynb` | Build and train a neural network in PyTorch |
| 9 | `09_neural_networks_with_tensorflow.ipynb` | Build and train the same network in TensorFlow (Keras) |
| 10 | `10_capstone_ml_project.ipynb` | Compare models and deliver a late-payment risk list |

## Files in this folder

- `generate_data.ipynb` - regenerates the synthetic dataset.
- `data/customer_accounts.csv` - the generated data used by every lesson.
- `models/` - created when you save a trained model (not committed to git).

## How to work through a notebook

Every notebook runs on its own: it loads the data and prepares it in its first cells.
Read each section, run the cells, and do the **Practice** before checking the
**Practice Solutions** at the bottom.
