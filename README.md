Santander Value Prediction Challenge
======================
This is my solution to the problem posted as part of the  [kaggle competition on identifying value of customer transactions.](https://www.kaggle.com/c/santander-value-prediction-challenge/)

 ![image](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/rel_images/santander_value_prediction_challenge_comp.png)

## Table of content

- [Overview](#overview)
- [Data](#data)
    - [Data Description](#data-description)
    - [File Descriptions](#file-descriptions)
- [Approach](#approach)
    - [First look at data](#first-look-at-data)
    - [Linear Regression](#linear-regression)    
    - [Principal Components Analysis](#principal-components-analysis)       
    - [Lasso](#lasso)            
    - [Random Forest using sklearn](#random-forest-using-sklearn)                
    - [Gradient boosting using sklearn](#gradient-boosting-using-sklearn)                    
    - [Gradient boosting using lightgbm](#gradient-boosting-using-lightgbm)                        
    - [Gradient boosting using h2o](#gradient-boosting-using-h2o)                            

## Overview

We have the following problem description from it's [corresponding kaggle competition link](https://www.kaggle.com/c/santander-value-prediction-challenge/overview/description) :
>According to Epsilon research, 80% of customers are more likely to do business with you if you provide personalized service. Banking is no exception.

>The digitalization of everyday lives means that customers expect services to be delivered in a personalized and timely manner… and often before they´ve even realized they need the service. In their 3rd Kaggle competition, Santander Group aims to go a step beyond recognizing that there is a need to provide a customer a financial service and intends to determine the amount or value of the customer's transaction. This means anticipating customer needs in a more concrete, but also simple and personal way. With so many choices for financial services, this need is greater now than ever before.

>In this competition, Santander Group is asking Kagglers to help them identify the value of transactions for each potential customer. This is a first step that Santander needs to nail in order to personalize their services at scale.

## Data

All the information pasted in this section has been obtained from the [this webpage (which shows data related information of the corresponding kaggle competition).](https://www.kaggle.com/c/santander-value-prediction-challenge/data)


### Data Description
 
You are provided with an anonymized dataset containing numeric feature variables, the numeric target column, and a string ID column. The task is to predict the value of target column in the test set.

### File Descriptions

- [train.csv](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/input/train.csv) - the training set.

- test.csv - the test set.

- [sample_submission.csv](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/input/test.csv) - a sample submission file in the correct format.

## Approach

The approach is to have a thorough look at the data, validate the same and decide on the path ahead.

### First look at data

This has been carried out in [take_a_look_at_data.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/first_look/take_a_look_at_data.ipynb). To summarize,  we went over the data, validated the same and decided to try out various modeling techniques starting with linear regression.

### Linear Regression

Linear Regression was [explored with various predictors](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/linear_regression/linear_regression.ipynb) and a cross validation score was computed over the entire training data set. Though, this did not yield us any notable prediction score on the test set(of 1.91), it was an important starting point and prompted us to inspect the heteroskedasticity of the predictors.

### Principal Components Analysis

Principal Components Analysis was [explored,](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/principal_components_analysis/principal_components_analysis.ipynb) both with original predictors as well as log transformed ones. This gave us a slight improvement on the prediction score on the test set to 1.87.

### Lasso

Lasso was [explored,](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/lasso/lasso.ipynb) and this gave us a minor bump in the prediction score on the test set to 1.75.

### Random Forest using sklearn

Random Forest was [implemented using sklearn package](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/random_forest/random_forest_sklearn.ipynb), and gave a us a major boost in the prediction score on the test set to 1.45.

### Gradient boosting using sklearn

Gradient boosting was [implemented using sklearn package](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/gradient_boosting/gradient_boosting_sklearn.ipynb), and gave us prediction score of 1.49 on the test set.

### Gradient boosting using lightgbm

Gradient boosting was [implemented using lightgbm package](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/gradient_boosting/gradient_boosting_lightgbm.ipynb), and gave us prediction score of 1.47 on the test set.

### Gradient boosting using h2o

Gradient boosting was [implemented using h20 package](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/modelling_approaches/gradient_boosting/gradient_boosting_h2o.ipynb), and gave us prediction score of 1.54 on the test set.
