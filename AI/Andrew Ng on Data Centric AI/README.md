# From Model-centric to Data-centric AI


Source: https://www.youtube.com/watch?v=06-AZXmwHjo&ab_channel=DeepLearningAI

----------------

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/ai%20cycle.PNG" alt="">
</p>

# Model-centric vs Data-centric AI

Basically, instead of trying to increase accuracy via a better model, go find better data (e.g. better label your data to avoid noise). This is because you can find a very good model via github and some good code snippet by e.g. stackoverflow, but this is not the case when it comes to **data** (which needs to be **customized** for your specific problem)

<br>

| Model-centric View | Data-centric View|
|-----|---------------------------------|
|Collect what data you can, and develop a model good enough to deal with the noise in the data (e.g. apply filters to remove noise ) |The consistency of the data is paramount. Use tools to improve the data quality; this will allow multiple models to do well|
|  Hold the data fixed and iteratively improve the code/model     | Hold the code fixed and iteratively improve the data   |

<br>

-----------------------

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/clean_noise.PNG" alt="">
</p>

------

Below: 
* E.g. you have collected 500 training examples. You can either now increase accuracy by cleaning your existing dataset, or you can collect more data to achieve that

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/no_of_training_data.PNG" alt="">
</p>

------


<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/data_vs_model_centric.PNG" alt="">
</p>



<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/data_vs_model_centric2.PNG" alt="">
</p>



<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/data_vs_model_centric3.PNG" alt="">
</p>

----------------------

# MlOps

AI Systems = Code + Data

<br>

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/ai_systems.PNG" alt="">
</p>

## MlOps vs DvOps

* The last figure in "traditional software" is about what <b>dvOps</b> do
* MLOps are the 3 figures in "AI software"

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/dvops_vs_mlops.PNG" alt="">
</p>

<br>

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/mlops_consistency.PNG" alt="">
</p>

<br>

<p align="center">
  <img src="https://github.com/dimi-fn/Online_Courses_Strath_et_etc/blob/master/Andrew%20on%20MLOps/img/big%20data_vs_good%20data.PNG" alt="">
</p>

----------------------------------------
# Notes to understand some of the above concepts

## Data drift & Concept drift

Sources: 

* https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/

* https://towardsdatascience.com/machine-learning-in-production-why-you-should-care-about-data-and-concept-drift-d96d0bc907fb


### Terminologies

**Data drift** (feature drift, population, or covariate shift): **change in data distributions**. the input data has changed, i.e. change in data distributions, and the model performs worse on unknown data regions.
* The distribution of the variables is meaningfully different
    * As a result, the trained model is not relevant for this new data. We need to train the model on the new data or rebuild it for the changes

**Concept drift**: **change in relationships**. The world has changed, and the model needs an update. It can be gradual (expected), sudden (you get it), and recurring (seasonal). In other words, when the patterns/relationships the model learned no longer hold. 
* In contrast to the data drift, the distributions (such as user demographics, frequency of words, etc.) might even remain the same. Instead, the relationships between the model inputs and outputs change.   

In other words: In some cases, the relationships between input and output data can change over time, therefore the function y=f(x) and subsequently our predictive model which assumed a static relationship between input and output will need to be updated ==>  `concept drift`
* In other domains, this change maybe called “covariate shift,” “dataset shift,” or “nonstationarity.”
* The first challenge is to detect when concept drift occurs. The second challenge is to keep the patterns up-to-date without inducing the patterns from scratch

For example, one concept in weather data may be the season that is not explicitly specified in temperature data, but may influence temperature data. Another example may be customer purchasing behavior over time that may be influenced by the strength of the economy, where the strength of the economy is not explicitly specified in the data. These elements are also called a “hidden context”.

Other examples of concept drift: 
* **Competitors launch new products**: Consumers have more choices, and their behavior changes. As should sales forecasting models.

* **Macroeconomic conditions evolve**. As some borrowers default on their loans, the credit risk is redefined. Scoring models need to learn it.

### Solutions

* Retrain the model using all available data, both before and after the change.
* Use everything, but assign higher **weights** to the new data so that model gives priority to the recent patterns.
* If enough new data is collected, we can simply drop the past.