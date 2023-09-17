# Statistics  


Contents
=======================

* [Descriptive vs. Inferential Statistics](#descriptive-vs-inferential-statistics)
* [The Central Limit Theorem (CTL)](#the-central-limit-theorem-ctl)
     * [Standard Deviation vs Standard Error](#standard-deviation-vs-standard-error)
     * [Normal Distribution and CTL](#normal-distribution-and-ctl)
* [Data Types](#data-types)
* [Distributions](#distributions)
* [Hypothesis Testing](#hypothesis-testing)
* [Correlation vs. Causation](#correlation-vs-causation)
* [Cheatsheets](#cheatsheets)

-----------------------------------------------------------------------------------------------------------



# Descriptive vs. Inferential Statistics

**Descriptive** statistics summarize the characteristics of a dataset.

**Inferential** statistics allow you to test a hypothesis or assess whether your data is generalisable to the broader population.

## Descriptive Statistics
Descriptive statistics refer to methods used to summarize and describe the main features of a dataset. The primary goal of descriptive statistics is to provide a concise and meaningful overview of the data, without making inferences or generalizations beyond the observed data. Descriptive statistics are used to understand the characteristics of the dataset and to gain insights into its central tendency, dispersion, and distribution.

* `Measures of central tendency`: Mean, median, and mode
* `Measures of dispersion`: Variance, standard deviation, range, interquartile range (IQR)
* `Measures of distribution`: Skewness and kurtosis.
* `Graphical representations`: Histograms, box plots, bar charts, scatter plots, etc.

All in all, descriptive statistics are useful for summarizing data, identifying patterns, detecting outliers, and providing initial insights into the dataset.

## Inferential Statistics
Inferential statistics, also known as differential statistics, involve making inferences or generalizations about a population based on a sample of data. The primary goal of inferential statistics is to draw conclusions beyond the observed sample and to assess whether differences or relationships observed in the sample are likely to exist in the broader population.

Inferential statistics use probability theory to estimate population parameters and test hypotheses. Key techniques include hypothesis testing, confidence intervals, and regression analysis. These methods help researchers determine whether observed differences or associations are statistically significant and not just due to random chance.

<br>In summary, descriptive statistics focus on summarizing and describing the characteristics of a dataset, while inferential statistics deal with making inferences about populations based on sample data

----------------------------------------------------

# The Central Limit Theorem (CTL)

The Central Limit Theorem (CLT) states that when you take a large enough sample size from a population (regardless of the population's underlying distribution), the distribution of the sample means will be approximately normally distributed.

In other words:
1. Imagine you have a population with any shape of distribution (skewed, uniform, or any other shape).
2. If you repeatedly take random samples of a certain size from this population and calculate the mean of each sample, the distribution of those sample means will tend to follow a normal (bell-shaped) curve as the sample size gets larger.
3. This means that even if the original population doesn't follow a normal distribution, the distribution of the sample means will become more and more like a normal distribution as you collect larger samples.

The CLT is a key concept in hypothesis testing, confidence intervals, and many other statistical methods because it allows us to make certain assumptions and perform various statistical tests, even when we don't know the exact shape of the population distribution, as long as our sample size is sufficiently large.

## Standard Deviation vs Standard Error

* The `standard deviation` measures the dispersion in the underlying population.
* The `standard error` measures the dispersion of the sample means (the standard error is the standard deviation of the sample means)
* A large standard error means that the sample means are spread out widely around the population
mean. Whereas a small standard error means that they are clustered relatively tightly

## Normal Distribution and CTL

Because the sample means are distributed normally (based on the CTL), it is always true that:
* we expect that 68% of all sample means will lie within 1 standard error of the population mean.
* 95% of the sample means will lie within 2 standard errors of the population mean.
* 99.7% of the sample means will lie within 3 standard errors of the population mean.

----------------------------------------------------

# Data Types

## Quantitative data (numeric data types)

* `Discrete data`
     * e.g., the number of students in a class, the number of employees in a compary
* `Continuous` data
     * e.g. The height of people, the speed of car

## Qualitative data (categorical data types)     
* `Nominal data` (they do not have any inherent order or numerical value associated with them)
     * e.g., gender (woman, man, etc)
     * e.g., hair colour (blonde, brown, etc)
     * e.g., ethnicity (english, asian, etc)
          * `Binomial data` (they specifically refer to a nominal variable that has only two categories or outcomes)
               * e.g., true/false, Yes/No responses, success/failure
* `Ordinal data`
     * e.g., first, second, third, etc
     * e.g., letter grades (a, b, c, etc)
     * e.g., economic status (low, medium, etc)

----------------------------------------------------


# Distributions

* [Statistical Distributions - by Data Science Infinity](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Maths%20-%20Statistics/Statistics/distributions.pdf)

----------------------------------------------------

# Hypothesis Testing

* Hypothesis Tests based on the data types of the dependent and independent variables:

![Hypothesis Tests based on the data types](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Maths%20-%20Statistics/Statistics/src/statistical_test_hypothesis_testing.jpg)


----------------------------------------------------


# Correlation vs. Causation

* [Correlation vs. Causation: Why Correlation Does Not Imply Causation](https://dimi-fn.github.io/portfolio/blog/articles/correlation.html)


----------------------------------------------------

# Cheatsheets

* [Statistics Cheatsheet by MIT](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Maths%20-%20Statistics/Statistics/Statistics_Cheatsheet_MIT.pdf)
* Statistics for Data Science - by Dharmaraj, [Part 1](https://medium.com/@draj0718/statistics-for-data-science-part-1-87eebc07698a), [Part 2](https://medium.com/@draj0718/statistics-for-data-science-part-2-ed532bc22ea4)


----------------------------------------------------


