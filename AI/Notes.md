# Notes

Contents 
=======================

* [Bias vs. Variance]()

------

## Bias vs. Variance Trade-Off

**Bias**: The assumptions taken by the model in order to predict the target function (mapping function)
* Low Bias: number of assumptions is small (e.g., Decision Trees, KNN, SVM)
* High Bias: number of assumptions is large (e.g., Linear Regression, Logistic Regression)

**Variance**: The amount of change in the mapping function when then training data changes
* Low Variance: Amount of change is small (e.g., Linear Regression, Logistic Regression)
* High Variance: Amount of change is large (e.g., Decision Trees, KNN, SVM)

Linear ML algorithms can often be trained fast (high bias <==> many assumptions), however with the downside of less flexibility in that they may not respond correctly when training data alters (low variance). On the other, non-linear ML models will often respond well to a change of the training dataset (high variance), however, with the trade-off of low bias.

There is always a monotonic relationship between bias and variance. The former cannot be reduced or increased without the opposite effect of the latter.

------

Sources

[1] [Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning - Jason Brownlee](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/)