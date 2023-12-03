# Notes on Machine Learning

Contents 
=======================

* [Definition of Machine Learning (ML)](#definition-of-machine-learning-ml)
* [Types of ML](#types-of-ml)
* [Types of ML Algorithms](#types-of-ml-algorithms)
     * [Supervised Learning](#supervised-learning)
          * [Types of Supervised Learning Algorithms](#types-of-supervised-learning-algorithms)
               * [Regression & Classification](#regression--classification)
               * [Multiple Linear Regression](#multiple-linear-regression)
               * [Polynomial Regression](#polynomial-regression)
     * [Unsupervised Learning](#unsupervised-learning)
          * [Types of Unsupervised Learning Algorithms](#types-of-usupervised-learning-algorithms)
     * [Common Notation in ML](#common-notation-in-ml)
* [Cost Function](#cost-function)
* [Gradient Descent](#gradient-descent)
* [ML Techniques](#ml-techniques)
     * [Vectorization](#vectorization)
     * [Feature Engineering](#feature-engineering)
* [Bias vs. Variance](#bias-vs-variance)

--------------------------------------------------------------------------------------------------

# Definition of Machine Learning (ML)

There are various definitions of Machine Learning (ML), one of those is that ML is considered a "Field of study that gives computers the ability to learn without being explicitly programmed" (Arthur Samuel, 1959).

-------------------------------------------------

# Types of ML

In general, there are three types of Machine Learning:

1. Based on `human supervision`:
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

#### Regression & Classification

* `Regression`
     * In regression, the objective is to predict a continuous variable as the output variable
          * e.g. linear regression
               * one example is linear regression with one variable (univariate linear regression)
     * There are infinitely many possible outputs
* `Classification`
     * In classification, the aim is to predict discrete categories/classes as the output.
          * the data is already labelled and we want to predict the class of unlabelled data
          * e.g. true/false, 0/1, red/green/green, success/failure, happiness/angry/sad/
     * There is a small number of possible outcomes    
          * **Binary classification**: the model outputs two possible classes (e.g., 0/1, no/yes, false/true)
          * `Logistic Regression`: The model's output is always in the range of 0 to 1, inclusive.
               * typically used for binary classification problems for predicting the probability of an instance belonging to a particular class 

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

#### Multiple Linear Regression

It is about applying linear regression when we have multiple features in the training set.

* f<sub>w,b</sub>(x) = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> +...+ w<sub>n</sub>x<sub>n</sub>+b,
where the **vector of w** containing all w (feature) cases and the **b** are the model *paremeters*

#### Polynomial Regression

While multiple linear regression assumes a linear relationship between the target variable and the input features, polynomial regression can capture more curved and nonlinear patterns in the data.

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

## Common Notation in ML

| Symbol |  Description | Common Python Variables|
|-----------|------------|----------------------|
| a   | scalar (non bold) | |
| **a**   | vector (bold) | |
| x   | input variable (the input feature) | x_train|
| y   | output variable (the predicted target) | y_train|
| m   | number of training examples from training set | m|
| n   | number of features in the training set | |
| w   | paremeter: weight |w |
| b   | parameter: bias | b|
| (x,y)   | single training example | |
| (x<sup>(i)</sup>, y<sup>(i)</sup>) | i<sup>th</sup> training example | x_i, y_i |
| (x<sup>(2)</sup>, y<sup>(2)</sup>) | the 2nd feature (input), not the exponent, from the training set, the 2nd target (output) from the training set ||
| f<sub>w,b</sub>(x) = wx+b = y, or simply f(x) = wx+b = y | function that takes `x` as input, and depending on the values of w and b, it will predict wx+b | |

<br>

attributes == features == predictors vs target variables == labels

-------------------------------------------------

# Cost Function

* The cost function tells us how well the model is performing so that we can improve it, in other words we far our target predictions are (y predicted) compared to the correct and real value (y true)
     * in linear regression, the most used cost function is the squared error cost function
* f<sub>w,b</sub>(x) = wx+b, where w,b parameters
     * w = weight (the slope of the function in the chart)
     * b = bias
          * w and b are parameters of the model, adjusted as the model learns from the data. They are also referred to as `coefficients` or `weights`
* In linear regression, we want to choose parameters w, b in such a way that the resulting linear function 'f' can effectively model and fit the given dataset.


<br>

Cost function in linear regression:

![Cost function in linear regression](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/AI/src/cost_function_linear_regression.PNG)

* The goal is to find such parameter values w and b, that will **minimize the cost function** `J`
 * When the cost is relatively small, closer to zero, it means the model fits the data better compared to other choices for w and b

-------------------------------------------------

# Gradient Descent

Gradient descent is an algorithm for finding values of parameters w and b that minimize the cost function J. We can apply gradient descent to try to minimize a wide range of cost functions, extending beyond the scope of linear regression functions where the cost function typically takes the form of a squared error cost function.
* The Gradient descent algorithm will search for the `local minima`, and by using Gradient Descent we want to find such parameters w, b, that will get us as close as possible to the global minimum.

* w = w-(a * (d/dw) J(w,b)), where
     * `a` is the **learning rate**, its usual range of values used are between 0 and 1
          * when a is close to zero, you take very small steps towards the local minimum. On the contrary, when a is close to 1, then you take larger steps across the function line, and in this latter case, you may fail to converge because you might overpass the local minimum
               * with a fixed learning rate, you adjust the **a** (in ascending order) to automatically take smaller steps when you start approaching the local minimum 
     * `w`,`b`: **parameters** 
          * update them *simultaneously* and repeat until convergence, i.e. until you reach one local minimum
               * when the cost function is the squared error cost, then there is always only one local minimum (global minimum)
     * `d/dw J(w,b)`: the **derivative** term


* `Batch` gradient descent: each step of the gradient descent uses *all* the training examples for each update step

* A good way to verify that gradient descent is working correctly is to look at the value of the cost function 𝐽(𝑤,𝑏) and check that it is decreasing with each step.

-------------------------------------------------

# ML Techniques
 
## Vectorization

Vectorization is a useful technique in data preparation for the implementation of ML algorithms where data is represented as vectors or matrices 
* `Scalars`:
     * **Definition**: A scalar is a single numerical value, without any direction, represented by a single number (e.g., 5, -2.3, 1000).
     * **Dimensionality**: zero dimensions: scalars represent only magnitude or size
     * **Examples**: Temperature, mass, speed, and time. E.g., 5 degrees Celsius is a scalar value representing temperature.
* `Vectors`:
     * **Definition**: A vector is a quantity that has both magnitude and direction, represented by an ordered list or array of numbers (e.g., [3, -1, 2]).
     * **Dimensionality**: Vectors have one or more dimensions: they represent quantities in multi-dimensional space.
     * **Examples**: Displacement, velocity, force, and electric field are examples of vector quantities. E.g., the velocity of an object is represented by a vector with components in the x, y, and z directions.
* `Matrices`: 
     * **Definition**: A matrix is a 2-dimensional array of numbers, e.g. [[1, 2], [3, 4], [5, 6]], i.e. it has rows and columns.
     * **Dimensionality**: Matrices have two dimensions (rows and columns): they are used for organizing and manipulating data in a grid-like structure.
     * **Examples**:  commonly used to represent linear transformations and to solve linear equations.

<br>

**Vectorization** is about:
* It is about the process of converting non-numeric data into a numerical format that they can be used by ML algorithms. 
* Requirement for vectorization to work: input data has to be in a numerical form
* The choice of vectorization technique depends on the nature of the data and the specific ML task. Effective vectorization can significantly impact the performance of a machine learning model.

```
f = np.dot(w,x) + b
```

where:
* w: parameter: weight
* x: input variable (the input feature)
* b: paremeter; bias

* The function above is a numpy function implementing a vectorized implementation of the dot product operation between two vectors, i.e. it implements the vectorized version of multipliying multiple pairs of parementers with their features (where that would look like: f = w[0]*x[0] + w[1] * x[1] +...+ b) so that it can run faster and more efficiently
* The reason it is faster is because the `np.dot` function from **NumPy** uses *parallel hardware* for computing to accelerate ML Jobs
     * vectors == lists of numbers == NumPy arrays

Examples where vectorization can be useful:      
* `Text Data`: Natural language processing (NLP) tasks involve processing text data. Vectorization techniques like TF-IDF (Term Frequency-Inverse Document Frequency) or word embeddings (e.g., Word2Vec, GloVe) are used to convert words or documents into numerical vectors.
* `Image Data`: Images are typically represented as pixel values. Convolutional Neural Networks (CNNs) and other image processing techniques convert images into numerical arrays or tensors, enabling machine learning models to work with them.
* `Categorical Data`: Machine learning models often require categorical variables (e.g., gender, color, country) to be one-hot encoded or label-encoded, turning them into binary or numeric representations
* `Time Series Data`: Time series data, such as stock prices or sensor readings, are usually transformed into numerical arrays where each element corresponds to a specific time point.
* `Feature Extraction`: Feature engineering involves creating new features or representations of data that are more informative for a particular task. Feature extraction techniques can create numerical features from raw data.
* `Dimensionality Reduction`: Techniques like Principal Component Analysis (PCA) or t-Distributed Stochastic Neighbor Embedding (t-SNE) transform high-dimensional data into lower-dimensional representations, making it easier to analyze and model

-------------------------------------------------

## Feature Engineering

Feature Engineering in Machine Learning might involve: 

* `Feature Scaling`
     * Feature scaling is a technique used to standardize or normalize the range of values in different features of the ML dataset. It typically involves transforming the data so that it falls within a specific range, e.g. between 0 and 1 or -1 and 1. 
     * It ensures that all features contribute equally to the learning process, meaning that all features have comparable value ranges. For instance, in a housing dataset, the scale of a column representing the number of bedrooms can be significantly different from the scale of a column representing the size of the house in square feet, hence we want to rescale them suitably.
          * ways to rescale the features: 
               * `standardization (z-score normalization)`
                    * After a **z-score normalization** implementation, all features will have a mean of 0 and a standard deviation of 1. 
               * `mean normalization`
               * `divide features by their max values` and use that range of values instead
                    * as a rule of thumb, keep the range of your features between [0, 1] or [-1, 1]. You don't want the range to be too large e.g. [60, 1053], or too small e.g [0.001, 0.01]
* `Feature Extraction`    
     * Feature extraction involves creating new features from existing column variables, by either transforming or combining the original features to create new ones. These new features may either replace the original ones during machine learning model training or be added to the dataset to enhance the model's understanding of the data (acting as better predictors in the model from the existing ones).
          * E.g. a car's mileage may exhibit a strong correlation with its age. In such a scenario, you can introduce a new feature, like a "wear and tear" variable, into the dataset. This additional feature has the potential to enhance the model's understanding and improve its performance in generating more accurate output results.

**Notes**: Feature engineering should be implemented not only in the training set but also in the test set for **consistency** and **generalization**. For instance, if you normalize the feature values in the training set, you should apply the same normalization to the test set. This ensures that the data presented in the test set maintains the same format as the training set (*consistency*). Additionally, this practice ensures that predictions made on the test set can be considered generalizable (*generalization*).

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
