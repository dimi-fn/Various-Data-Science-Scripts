# Notes on Machine & Deep Learning

Contents 
=======================

* [Definition of Machine Learning (ML)](#definition-of-machine-learning-ml)
* [Types of ML](#types-of-ml)
* [Types of ML Algorithms](#types-of-ml-algorithms)
     * [Supervised Learning](#supervised-learning)
          * [Types of Supervised Learning Algorithms](#types-of-supervised-learning-algorithms)
               * [Regression](#regression)
               * [Classification](#classification)
     * [Unsupervised Learning](#unsupervised-learning)
          * [Types of Unsupervised Learning Algorithms](#types-of-usupervised-learning-algorithms)
     * [Common Notation in ML](#common-notation-in-ml)
* [Cost & Loss Function](#cost--loss-function)
* [Bias vs. Variance](#bias-vs-variance)
* [Gradient Descent & Optimization Algorithms](#gradient-descent--optimization-algorithms)
* [ML Techniques](#ml-techniques)
     * [Vectorization](#vectorization)
     * [Feature Engineering](#feature-engineering)
     * [Regularization](#regularization)
* [Model Evaluation & Selection](#model-evaluation--selection)
* [Activation Functions & Decision Boundaries](#activation-functions--decision-boundaries)
* [ML Development & Cycle](#ml-development--cycle)
* [Deep Learning](#deep-learning)
     * [Neural Network Layers](#neural-network-layers)
     * [Forward & Back Propagation](#forward--back-propagation)
     * [Tensorflow](#tensorflow) 

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

#### Regression

`Regression`
* In regression, the objective is to predict a continuous variable as the output variable
     * e.g. `linear regression`
          * one example is linear regression with one variable (univariate linear regression)
* There are infinitely many possible outputs

`Multiple Linear Regression`

It is about applying linear regression when we have multiple features in the training set.

* f<sub>w,b</sub>(x) = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> +...+ w<sub>n</sub>x<sub>n</sub>+b,
where the **vector of w** containing all w (feature) cases and the **b** are the model *paremeters*

`Polynomial Regression`

While multiple linear regression assumes a linear relationship between the target variable and the input features, polynomial regression can capture more curved and nonlinear patterns in the data.     

#### Classification

`Classification`
* In classification, the aim is to predict discrete categories/classes as the output.
     * the data is already labelled and we want to predict the class of unlabelled data
     * e.g. true/false, 0/1, red/green/green, success/failure, happiness/angry/sad/
* There is a small number of possible outcomes    
     * **Binary classification**: the model outputs two possible classes (e.g., 0/1, no/yes, false/true)
     * `Logistic Regression`: The model's output is always in the range (0, 1), exclusive
          * typically used for binary classification problems for predicting the probability of an instance belonging to a particular class 
* `Multiclass Classification`: a classification problem where each input data point can belong to more than one class, e.g. predicting if an animal is dog, cat, dolphin etc
     * `Softmax` mathematical function is particularly useful in multiclass classification problems, where an input can belong to one of several classes. Using a softmax output layer helps in making the network's predictions more interpretable and suitable for decision-making based on probabilities.
          * used in conjunction with **loss = SparseCategoricalCrossentropy**
               * or **loss = SparseCategoricalCrossentropy(from_logits=True)** by using a linear (and not softmax) output layer for a more accurate implemtation of softmax
* `Multi-label Classification`: In multilabel classification, each instance can be assigned to multiple classes or labels simultaneously.
     * e.g., a document can be about "Science," "Technology," and "Environment" at the same time.
     * an emotion can be both tagged and classified as 'fear' and 'sadness' for a particular input instance
     * on the street at a specific timestamp, there could be a car, a bus, and a pedestrian at the same time.
* A problem can be both a multilabel and multiclass classification task
     * example: collection of articles, and the goal is to classify them into both overarching topics (multiclass) and specific themes discussed in the articles (multilabel).
          * Multiclass Aspect: Classes for overarching topics: "Technology," "Health," "Science," and "Business"
          * Multilabel Aspect: Labels for specific themes: "Artificial Intelligence," "Marketing", "Climate Change," "Entrepreneurship" and "Mobile Technology"
          * Each article can belong to one of the broader topics (multiclass), such as "Technology," while also addressing multiple specific themes (multilabel), like "Artificial Intelligence" and "Entrepreneurship" at the same time.

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

-------

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

# Cost & Loss Function

* In ML, the terms "`cost function`" and "`loss function`" are often used interchangeably, but their difference lies in the fact that the loss function is applied to individual data points and measures the error for each prediction, while the cost function is an aggregate measure of the overall model performance across the entire dataset. 
* The cost function tells us how well the model is performing so that we can improve it, or in other words and more specifically, it indicates how far the target predictions are (**y predicted**) compared to the correct and real values (**y true**)
     * in linear regression, the most used cost function is the squared error cost function
* f<sub>w,b</sub>(x) = wx+b, where w,b parameters
     * w = weight (the slope of the function in the chart)
     * b = bias
          * w and b are parameters of the model, adjusted as the model learns from the data. They are also referred to as `coefficients` or `weights`
* In linear regression, we want to choose parameters w, b in such a way that the resulting linear function 'f' can effectively model and fit the given dataset.


## Linear Regression

The typical cost function for linear regression is the Mean Squared Error (`MSE`), with the Root Mean Squared Error (`RMSE`) being the common metric for evaluating the performance of a linear regression model.

![Cost function in linear regression](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/AI/src/cost_function_linear_regression.PNG)

* The goal is to find such parameter values w and b, that will **minimize the cost function** `J`
 * When the cost is relatively small, closer to zero, it means the model fits the data better compared to other choices for w and b


## Logistic Regression
* In logistic regression, the cost function is the Cross-Entropy Loss (`Log Loss`), also known as the `logistic loss function`, which is more suitable for the categorization task where the target is 0 or 1 rather than any number as in linear regression.
* The square root is not a good cost function in logistic regression because it doesn't exhibit the convex properties needed for efficient optimization, leading to multiple local minima and making it difficult to find the global minimum efficiently. However, by using the loss function, the overall cost function will get convex, and hence, we can use the gradient descent to take us to the global minimum.
* `Evaluation metrics`: The common evaluation metrics for logistic regression include Accuracy (the proportion of correctly classified instances), Precision, Recall, and F1 Score.

-------------------------------------------------

# Bias vs. Variance

`Bias`: The assumptions taken by the model in order to predict the target function (mapping function)
* **Low Bias**: number of assumptions is small (e.g., Decision Trees, KNN, SVM)
* **High Bias**: number of assumptions is large (e.g., Linear Regression, Logistic Regression) --> `underfit` (underfits the dataset) --> the model is not even doing well in the training set
     * Solutions to fix the high variance problem:
          * incorporate additional features
          * try adding polynomial features
          * try decreasing the regularization parameter λ

`Variance`: The amount of change in the mapping function when then training data changes
* **Low Variance**: Amount of change is small (e.g., Linear Regression, Logistic Regression)
* **High Variance**: Amount of change is large (e.g., Decision Trees, KNN, SVM) --> `overfit` (overfits the dataset, i.e. the model is worse in the cross validation set than the training set (cross validation error >> training error), or in other words, the model is very good at the data that has seen, but not in the data that it hasn't seen)
     * Solutions to fix the high variance problem: 
          * get more training examples
          * try smaller set of features
          * try increasing the regularization parameter λ

Linear ML algorithms can often be trained fast (high bias <==> many assumptions), however with the downside of less flexibility in that they may not respond correctly when training data alters (low variance). On the other, non-linear ML models will often respond well to a change of the training dataset (high variance), however, with the `trade-off` of low bias.

Ideally, we'd like to have both low bias and variance, but there's always a `bias-variance trade-off` relationship found, i.e. bias cannot be reduced or increased without the opposite effect of variance, and vice versa. Since the ideal case is not feasible, we seek the situation where both bias and variance are somewhere in the middle. As a result, the goal is to achieve a balance between bias and variance to build a model that generalizes well to unseen data.
* We want low bias: so that the model is flexible enough to capture the underlying patterns in the training data
* We want low variance: so that the model is not too sensitive to the specific training data and can generalize well to new unseen data

Reminder that:
* `Overfitting` the dataset: high variance and low bias
* `Underfitting` the dataset: high bias and low variance

-------------------------------------------------

# Gradient Descent & Optimization Algorithms

## Gradient Descent

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
          * A `derivative` measures how a function changes as its input changes. In ML, derivatives are used to find the slope (rate of change) of a function. This is useful for adjusting model parameters to minimize errors or improve performance during training.
               * via the 'symbolic' derivative, you can find the value of the derivative at any input value 𝑤
 .


* `Batch` gradient descent: each step of the gradient descent uses *all* the training examples for each update step

* A good way to verify that gradient descent is working correctly is to look at the value of the cost function 𝐽(𝑤,𝑏) and check that it is decreasing with each step.

## Adam Optimization Algorithm

Adam (short for Adaptive Moment Estimation) is an optimization algorithm commonly used in ML to efficiently update the parameters of a model during training. It adjusts the learning rates for each parameter individually based on their historical gradients and helps accelerate convergence.

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

## Regularization

Regularization techniques can be used to tackle common problems in ML, e.g. to reduce overfitting or underfitting.

* `Overfitting` is a common issue in ML where the model might perform well (or even very well) on the training set but may fail when it faces new, unseen data. This happens when the patterns and the noise in the training set do not generalize well in the whole dataset, and the model learns only from the specific patterns and noise found in the underlying training part of the dataset. Overfitting results in `high variance`, because the same model used across different but similar datasets might product highly variable predictions, i.e. and e.g. running the same model on a slightly different input value might give a very different output value. Possible solutions here is to remove noise by removing some of the features that might not help the model generilize well.
     * overfitting (too many input x features) --> high variance
          * solutions: 
               * data cleaning and preprocessing
               * increase the training data
               * feature selection & feature extraction: exclude non-useful features (that might bring noise), select (feature selection), or generate (feature extraction) the most important input features
               * **bias and variance as a function of regularization parameter (λ)**: apply regularization: in order to reduce the overfitting impact of some of the features  without having to eliminate them by reducing the size of the parameters that can be achieved by penalizing then (using the λ legularization parameter)
                    * when a model needs regularization, then if l=0, the model will overfit as previously (nothing has changed), and if l is a very big number, then conversely, the model will turn to have an underfitting problem instead (increasing the **regularization parameter** `λ` will decrease the size of the model parameters, but increasing **λ** too much, it will decrease the model parameters close to 0, turning the function to be equal only with the parameter b (bias))
* `Underfitting` is the opposite of overfitting. It happens when a ML model is too simple to capture the underlying patterns in the training data. In other words, the model struggles to grasp the relationships between inputs and outputs, resulting in a poor fit to both the training set and new, unseen data. Typically, underfit models exhibit `high bias`; e.g., a simple linear function predicting housing prices may have high bias if it always predicts an increase in price as the house size increases, disregarding other relevant factors. In this case, we'd say that the model presents a high bias (preconception) in the relationship between the inputs (house size) and the output (price) where the model assumes that the house prices are going to be a completely linear function of the house sizes, i.e. it oversimplifies the relationship by assuming that the only factor influencing the price is the size of the house (in that case, adding more inputs, like the area zone of the house, would help reduce underfitting).
     * underfitting (too few input x features) --> high bias
          * solutions
               * data cleaning and preprocessing
               * increase the training data
               * increase model complexity (e.g. instead of using a linear model, switch to e.g. decision tree or SVM, random forest, neural networks)
               * feature engineering: transform existing features or add relevant features to better represent the underlying patterns of the data
               * reduce regalurization

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
          * note: when you the model on scaled values, you should also feed in the scaled training set instead of its raw values, by using the same scaling method used in the training set
* `Feature Extraction`    
     * Feature extraction involves creating new features from existing column variables, by either transforming or combining the original features to create new ones. These new features may either replace the original ones during machine learning model training or be added to the dataset to enhance the model's understanding of the data (acting as better predictors in the model from the existing ones).
          * E.g. a car's mileage may exhibit a strong correlation with its age. In such a scenario, you can introduce a new feature, like a "wear and tear" variable, into the dataset. This additional feature has the potential to enhance the model's understanding and improve its performance in generating more accurate output results.

**Notes**: Feature engineering should be implemented not only in the training set but also in the test set for **consistency** and **generalization**. For instance, if you normalize the feature values in the training set, you should apply the same normalization to the test set. This ensures that the data presented in the test set maintains the same format as the training set (*consistency*). Additionally, this practice ensures that predictions made on the test set can be considered generalizable (*generalization*).

------------------------------------------------

# Model Evaluation & Selection

* Split the dataset into a training and a test set
     * however, a better method is splitting the dataset into 3 parts: training part/cross validation part (development part)/ test set
          * e.g. training set 60%, cross validation 20%, test set 20% of the dataset and you can evaluate and compute the cross validation error too
          * Cross-validation provides a more reliable estimate of a model's performance by using different subsets of data for training and testing. This helps ensure that the evaluation is not overly dependent on a specific random split of data
* Compute the test error to report the model's generalization error and to understand how well the ML model is performing on the test part of the dataset
     * You can also compute the training error, although the test error would be more useful for judging how well the model can generalize to new data
* When selecting a model, you want to choose one that performs well both on the training and cross validation set. It implies that it is able to learn the patterns from your training set without overfitting 

------------------------------------------------

# Activation Functions & Decision Boundaries

## Activation Functions 

* `Sigmoid function` (`logistic function`): it is an activation function in ML (S shape) that transforms any number values between 0 and 1 in order to get output probabilities that express the probability that a particular output belongs to a particular class.
     * In the sigmoid function, the variable z represents the input to the function. The function approaches 0 as z goes to large negative values and approaches 1 as z goes to large positive values.
     * it is commonly used in binary classification problems to transform a linear combination of input features into probabilities
* In Deep Learning, apart from the sigmoid function, one common activation function is the linear activation function, but one of the most common activation functions is the `ReLU` (Rectified Linear Unit)    
     * ReLU introduces non-linearity to the network, allowing it to learn complex patterns in the data (i.e. it can learn from non-linear relationships in the data)

* Choosing activation functions
     * You can choose different activation functions across the different layers within the same neural network
          * Binary classification problem: sigmoid activation function
          * Regression problem where output can take either negative or positive values: linear aggregation function
          * Regression problem where output>=0: ReLU


## Decision Boundaries

* The `decision boundary` represents the threshold at which a model makes predictions about the class to which a new input belongs. Instances on one side of the decision boundary are assigned to one class, while instances on the other side are assigned to a different class. The goal of a ML training model is to find the optimal decision boundary that minimizes classification errors and generalizes well to new unseen data.

-------------------------------------------------

# ML Development & Cycle

* Scope project
* Collect data
* Choose architecture (model, data, etc.)
* Iterative process loop 
     * Train the model (training process)
          * Conduct model diagnostics (bias, variance, and error analysis) & iterative improvement
               * Error analysis in ML involves examining and understanding the mistakes made by a model to improve its performance. It includes identifying the types of errors (false positives, false negatives, etc.), analyzing patterns in misclassifications, and determining the root causes of inaccuracies. In this way we can make adjustments, refine the algorithm, or gather more relevant data to enhance overall accuracy and effectiveness. Essentially, error analysis helps fine-tune the ML model for better results.
     * Adding data
          * Data of the types where error analysis has indicated it might help
          * Data augmentation
               * Modifying an existing training example to create new training example (e.g. rotating the images that are the inputs of the training set)
     * Transfer Learning
          * Supervised pre-training
          * Fine-tuning
* Deploy in production
     * You might need to go back to the 2nd step of collecting data

-------------------------------------------------

# Deep Learning

## Neural Network Layers

* `Layers`: A layer is a grouping of neurons that takes as input the same or similar inputs and it produces the output layer. Neural networks are composed of layers stacked on top of each other, and each layer performs a specific type of computation. Each neuron in a layer is connected to every neuron in the adjacent layers. The strength of these connections, known as weights, is adjusted during the training process to enable the network to make accurate predictions or classifications. There are 3 main types of layers:
     * `Input Layer` (layer 0): The first layer that receives the input data. Each neuron in this layer represents a feature in the input data, and hence the input layer turns to be a vector of input features.
     * `Hidden (Dense) Layers` (layer 1, 2, and so on): Intermediate layers between the input and output layers where computations are performed. Each hidden layer might carry a different number of neurons (input units), and each neuron processes information from the previous layer and passes it on to the next, i.e. and e.g., the output of layer 1 becomes the input of layer 2, and so on.
          * Every neuron in a **dense** layer gets as its inputs all the activations from the previous layer
     * `Output Layer`: The final layer that produces the network's output. The number of neurons in this layer depends on the type of problem (e.g., one neuron for binary classification, multiple neurons for multi-class classification).
          * the combination of the above is called '`multilayer perceptron (MLP)`', which is basically the neural network for supervised learning
          * when we say we have 4 input layers, then we implicitly mean we have 3 hidden (intermediate) layers and 1 output layer- the input layer, layer 0, is not counted
* `Architecture of a neural network`     
     * decision about: the number of hidden layers, the number of hidden units (neurons) per layer
     * A `computation graph` is a visual representation of the mathematical operations (`nodes`) and their dependencies (`edges`) in a deep learning model. It shows how data flows through the network, from input to output, capturing the sequence of computations.

## Forward & Back Propagation

Forward propagation is about making predictions, while backward propagation is about learning from those predictions and updating the network to make better predictions in the future. Both forward and backward propagation are essential, and they work together in an iterative process:

* `Forward Propagation`: This is the process of passing input data through the network to obtain the predicted output. The input data is fed into the input layer, and it travels through each hidden layer until it reaches the output layer. Neurons in each layer perform weighted sums and apply activation functions to produce the output. The predicted output is then compared to the actual output to calculate the loss.
* `Back Propagation`: This is the process of updating the weights of the neural network to minimize the difference between the predicted output and the actual output. It involves calculating the gradient of the loss with respect to the weights and adjusting the weights accordingly. This is done using optimization algorithms like Gradient Descent. In order words, via backpropagation we can compute the derivatives for Gradient Descent.

## Tensorflow

While Scikit-learn focuses on traditional ML algorithms (e.g. classification, regression, clustering, dimensionality reduction, model selection), TensorFlow is also an open-source ML library used to build and train ML models, particularly deep learning models.

In TensorFlow, a `tensor` is a data structure representing multi-dimensional arrays or matrices. Tensors can have different ranks, which correspond to the number of dimensions they possess.
* `Scalar` (rank 0): A single numerical value, e.g. 5
* `Vector` (rank 1): An array of scalars, like a list of numbers, e.g. [2,3,4]
* `Matrix` (rank 2): A 2D array of numbers arranged in the shape of rows and columns
     * Tensors can easily be converted to numpy arrays via np.array()

* `Step 1`
     * Data preprocessing 
          * data cleaning
          * handling missing data
          * data encoding
               * converting categorical variables into numerical representations
          * feature engineering
               * creating new features or transforming existing ones to enhance the model's performance
          * Data normalization/scaling: .g. normalize the data (tf.keras.layers.Normalization)
* `Step 2: Define the model`

```
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
```

* `model.Sequential`([layer_1, layer_2, ...])
* `model.summary()`: summary of the model

* `Step 3: compile the model`
     * Compile the model and specify the loss function used (i.e. the way of measurement of how far off the predicted output is from the actual output)
     * `model.compile`(loss= )
* `Step 4: fit the model`
     * Train the model
     * `model.fit`(x,y, epochs= integer number)
          * epochs in neural networks are like the steps that we need to decide for the learning algorithm to run (e.g. gradient descent) 
* `Step 5: Make model prediction`
     * Make the model predictions
     * `model.predict`(x_new)

-------------------------------------------------

Sources

* [1] [Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning - Jason Brownlee](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/)
* [2] [Machine Learning Specialization - by Andrew Ng](https://www.deeplearning.ai/courses/machine-learning-specialization/)
