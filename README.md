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
    - [Building simple models](#building-simple-models)    

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

This has been carried out in [take_a_look_at_data.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/first_look/take_a_look_at_data.ipynb). To summarize,  we went over the data, validated the same and concluded that nature of data itself warrants training of a lasso model on the same as the starting step.

### Building simple models

Lasso models have been constructed in the [R programming language](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/lasso_models/r_code/lasso.R) and predictions have been made over test data using [Python](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/lasso_models/predict_with_lasso_model_from_coefficients.ipynb). While this was a good starting point, the models themselves do not look to be providing us with much predictive power, as the prediction scores over the test set were only around 5.5.

However, things looked a lot better when lasso models were constructed in [Python.](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/lasso_models/lasso_in_python.ipynb), giving us a test score of around 1.99 while trained with the optimal value of the lasso parameter, which in turned was obtained by cross validation on the training set.
