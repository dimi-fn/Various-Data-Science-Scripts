# Notes on Machine Learning

Contents 
=======================

* [Definition of ML](#definition-of-ml)
* [Types of ML](#types-of-ml)
* [Types of ML Algorithms](#types-of-ml-algorithms)
* [Bias vs. Variance](#bias-vs-variance)

--------------------------------------------------------------------------------------------------

# Definition of ML

There are various definitions of Machine Learning, one of those is that ML is considered a "Field of study that gives computers the ability to learn without being explicitly programmed" (Arthur Samuel, 1959)

-------------------------------------------------

# Types of ML

In general, there are 3 types of ML:

1. Based on human supervision:
* supervised, unsupervised, semi-supervised, reinforcement learning

2. Whether or not the ML model can learn incrementally or on the fly
* `online learning` vs `batch learning`

3. Whether the ML model works
* by comparing new data points to known (`instance-based learning`)
* by detecting patterns in the training data and building a predictive model (`model-based learning`)

-------------------------------------------------

# Types of ML Algorithms

## Supervised Learning

Algorithms that learn from input (x) examples to predict output (y) result

| Input (x) | Output (y) | Application |
|-----------|------------|-------------|
| email   | spam? (0/1)   | spam filtering      |
| audio  | text transcripts   | speech recognition   |
| english   | spanish   | machine translation  |
| ads, user info   | click? (0/1)   | online advertisting |


## Unsupervised Learning


-------------------------------------------------


# Bias vs. Variance

**Bias**: The assumptions taken by the model in order to predict the target function (mapping function)
* Low Bias: number of assumptions is small (e.g., Decision Trees, KNN, SVM)
* High Bias: number of assumptions is large (e.g., Linear Regression, Logistic Regression)

**Variance**: The amount of change in the mapping function when then training data changes
* Low Variance: Amount of change is small (e.g., Linear Regression, Logistic Regression)
* High Variance: Amount of change is large (e.g., Decision Trees, KNN, SVM)

Linear ML algorithms can often be trained fast (high bias <==> many assumptions), however with the downside of less flexibility in that they may not respond correctly when training data alters (low variance). On the other, non-linear ML models will often respond well to a change of the training dataset (high variance), however, with the `trade-off` of low bias.

There is always a monotonic relationship between bias and variance. The former cannot be reduced or increased without the opposite effect of the latter.

-------------------------------------------------

Sources

* [1] [Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning - Jason Brownlee](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/)
* [2] [Machine Learning Specialization - by Andrew Ng](https://www.deeplearning.ai/courses/machine-learning-specialization/)
