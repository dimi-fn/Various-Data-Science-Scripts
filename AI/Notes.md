# Notes on Machine Learning

Contents 
=======================

* [Definition of ML](#definition-of-ml)
* [Types of ML](#types-of-ml)
* [Types of ML Algorithms](#types-of-ml-algorithms)
     * [Supervised Learning](#supervised-learning)
          * [Types of Supervised Learning Algorithms](#types-of-supervised-learning-algorithms)
     * [Unsupervised Learning](#unsupervised-learning)
          * [Types of Unsupervised Learning Algorithms](#types-of-usupervised-learning-algorithms)
     * [Notation in ML](#notation-in-ml)
* [Bias vs. Variance](#bias-vs-variance)

--------------------------------------------------------------------------------------------------

# Definition of ML

There are various definitions of Machine Learning (ML), one of those is that ML is considered a "Field of study that gives computers the ability to learn without being explicitly programmed" (Arthur Samuel, 1959)

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

Algorithms that perform supervised learning, learn from input (x) examples (the "right answers", the features) to predict output (y) result (the target variable) (i.e., they implement x to y mappings), e.g. linear **regression**, **classification**.

### Types of Supervised Learning Algorithms

* `Regression`
     * In regression, the objective is to predict a continuous variable as the output variable
     * There are infinitely many possible outputs
* `Classification`
     * In classification, the aim is to predict discrete categories/classes as the output.
          * e.g. true/false, 0/1, red/green/green, success/failure, happiness/angry/sad/
     * There is a small number of possible outcomes     

| Input (x) | Output (y) | Application |
|-----------|------------|-------------|
| email   | spam? (0/1)   | spam filtering      |
| audio  | text transcripts   | speech recognition   |
| english   | spanish   | machine translation  |
| ads, user info   | click? (0/1)   | online advertisting |
| image, radar info etc   | position of other cars   | self-driving car |


**Example problems**:
* Given email labeled as spam/not spam, learn a spam filter (classification)
* Given a dataset of patients diagnosed as either having diabetes or not, learn to classify new patients as having diabetes or not (classification)


## Unsupervised Learning
While in supervised learning the model learns from data labeled with the "right answers" and comes with inputs **x** (features), in **unsupervised** learning the data comes only with inputs **x** without the **y** outputs, and we are trying to find out insteresting patterns structured in a particular dataset (without having existing labels in the dataset)

**Example problems**:
* Given a set of news articles found on the web, group them into sets of articles about the same stories.
* Given a database of customer data, automatically discover segments and group customers into different market segments.

### Types of Unsupervised Learning Algorithms

* `Clustering`
     * Takes data without labels and tries to automatically group them into clusters
* `Anomaly detection`     
     * Finds unusual data points
* `Dimensionality Reduction`     
     * Compresses data using fewer numbers

## Notation in ML

| Symbol |  Description |
|-----------|------------|
| x   | input variable (the input feature) | 
| y   | output variable (the predicted target) | 
| m   | number of training examples from training set | 
| (x,y)   | single training example | 
| (x<sup>(i)</sup>, y<sup>(i)</sup>) | i<sup>th</sup> training example |
| (x<sup>(2)</sup>, y<sup>(2)</sup>) | the 2nd feature (input) from the training set, the 2nd target (output) from the training set |
| f<sub>w,b</sub>(x) = wx+b, or simply f(x) = y  | function that takes `x` as input, and depending on the values of w and b, it will predict a `y` value| 



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
