Santander Value Prediction Challenge
======================
This is my solution to the problem posted as part of the  [kaggle competition on identifying value of customer transactions.](https://www.kaggle.com/c/santander-value-prediction-challenge/)

 ![image](https://github.com/babinu-uthup-4JESUS/Kaggle_Santander_Value_Prediction_Challenge/blob/master/rel_images/santander_value_prediction_challenge_comp.png)

## Table of content

- [Overview](#overview)
- [Data](#data)
    - [Data Description](#data-description)
    - [File Descriptions](#file-descriptions)
    - [Data Fields](#data-fields)    
- [Approach](#approach)
    - [Data Validation](#data-validation)
    - [Building simple models](#building-simple-models)
- [More Complex models](#more-complex-models)
    - [Gradient boosting using tensorflow](#gradient-boosting-using-tensorflow)
    - [Gradient boosting using xgboost](#gradient-boosting-using-xgboost)
    - [DNN using tensorflow](#dnn-using-tensorflow)    
    - [Addition of new variables to the xgboost method](#addition-of-new-variables-to-the-xgboost-method)
- [Important note regarding creation of training and validaion sets](#important-note-regarding-creation-of-training-and-validaion-sets)
    - [Gradient_boosting_on_new_dataset](#gradient-boosting-on-new_dataset)
    - [DNN_on_new_dataset](#dnn-on-new_dataset)
- [Final-conclusion](#final-conclusion)

## Overview

We have the following problem description from it's [corresponding kaggle competition link](https://www.kaggle.com/c/santander-value-prediction-challenge/overview/description) :
>According to Epsilon research, 80% of customers are more likely to do business with you if you provide personalized service. Banking is no exception.

>The digitalization of everyday lives means that customers expect services to be delivered in a personalized and timely manner… and often before they´ve even realized they need the service. In their 3rd Kaggle competition, Santander Group aims to go a step beyond recognizing that there is a need to provide a customer a financial service and intends to determine the amount or value of the customer's transaction. This means anticipating customer needs in a more concrete, but also simple and personal way. With so many choices for financial services, this need is greater now than ever before.

>In this competition, Santander Group is asking Kagglers to help them identify the value of transactions for each potential customer. This is a first step that Santander needs to nail in order to personalize their services at scale.

## Data

All the information pasted in this section has been obtained from the [this webpage (which shows data related information of the corresponding kaggle competition).](https://www.kaggle.com/c/competitive-data-science-predict-future-sales/data)


### Data Description
 
You are provided with daily historical sales data. The task is to forecast the total amount of products sold in every shop for the test set. Note that the list of shops and products slightly changes every month. Creating a robust model that can handle such situations is part of the challenge.

### File Descriptions

- [sales_train.csv](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/input/sales_train.csv) - the training set. Daily historical data from January 2013 to October 2015.

- [test.csv](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/input/test.csv) - the test set. You need to forecast the sales for these shops and products for November 2015.

- [sample_submission.csv](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/input/sample_submission.csv) - a sample submission file in the correct format.

- [items.csv](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/input/items.csv) - supplemental information about the items/products.

- [item_categories.csv](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/input/item_categories.csv) - supplemental information about the items categories.

- [shops.csv](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/input/shops.csv) - supplemental information about the shops.

### Data fields

- ID                 - an Id that represents a (Shop, Item) tuple within the test set
- shop_id            - unique identifier of a shop
- item_id            - unique identifier of a product
- item_category_id   - unique identifier of item category
- item_cnt_day       - number of products sold. You are predicting a monthly amount of this measure
- item_price         - current price of an item
- date               - date in format dd/mm/yyyy
- date_block_num     - a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
- item_name          - name of item
- shop_name          - name of shop
- item_category_name - name of item category

## Approach

The approach is to have a thorough look at the data, validate the same and try out relevant modeling techiniques. 

### Data Validation

This has been carried out in [data_sanity_check.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/data_sanity_check/data_sanity_check.ipynb). To summarize, we have done the following :

- Data sanity test                          - to make sure that we do not have unexpected input.
- Conversion to monthly data                - to facilitate easier data processing in the future.
- Evaluation of a simple past average model - to serve as a benchmark for later models.

### Building simple models

This has been carried out in [data_analysis_and_models.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/data_analysis_and_models/data_analysis_and_models.ipynb). I am summarizing the models briefly below :

- Model 1 - takes the value of the previous month for the corresponding shop and item if present, 1 if absent (Score : 2.37) .
- Model 2 - takes the value of the most recent month in the past if available, 1 if not (Score : 2.42).
- Model 3 - bayesian model which takes 1 as the prior and historical value for the most recent month as the posterior, and 
            combines the same using recency weighting (Score : 2.37).
- Model 4 - take the average of the previous month for the corresponding shop and item if present, the average of the item 
            across different shops for the previous month if absent. If both of these are unavailable, value is set to 1 (Score 
            : 2.71).

Thus, though Model 3 was marginally better than the rest, Model 1 score in terms of simplicity.

NOTE : In all these cases, we have fixed the data for the first 32 months as the traininig set, data for the month of 33 as the validation data set and the data for the month of 34 as the test set.

## More Complex models

In this section, we experiment with more complex model architectures such as gradient boosting, random forest and so on.

### Gradient boosting using tensorflow
This has been implemented in  [gradient_boosting_tensorflow.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/gradient_boosting_tensorflow.ipynb). It does not look to offer much benefit as the best score which we were able to obtain was 2.61.

### Gradient boosting using xgboost
This has been implemented in [gradient_boosting_xgboost.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/gradient_boosting_xgboost.ipynb). It gave us a reasonably good improvement as we got a score of 2.27 on the validation set.

### DNN using tensorflow
This has been implemented in [dnn_tensorflow.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/dnn_tensorflow.ipynb). It did not help much and gave a mediocre score of 2.60 (NOTE: Since this method involved more processing, this was executed as a [kaggle kernel](https://www.kaggle.com/babinu/predict-sales-tensorflow?scriptVersionId=20825161)).

### Addition of new variables to the xgboost method
This has been implemented in [gradient_boosting_using_xgboost_new_variables.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/more_complex_models/gradient_boosting_using_xgboost_new_variables.ipynb). This gave us some improvement to 2.15 and was executed as a [kaggle kernel](https://www.kaggle.com/babinu/gradient-boosting-using-xgboost-new-variables?scriptVersionId=20826601) to improve running speed.

### LSTM using keras
This has been implemented in [lstm_keras.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/more_complex_models/lstm_keras.ipynb). It did not help much and gave a mediocre score of 2.27 (NOTE: Since this method involved more processing, this was executed as [kaggle kernel](https://www.kaggle.com/babinu/lstm-keras?scriptVersionId=20831177)).

### Xgboost on all previous months' data
This has been implemented in [gradient_boosting_using_xgboost_new_variables.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/more_complex_models/gradient_boosting_using_xgboost_new_variables.ipynb). This did not give us much of improvement as the score remained at 2.24 and was executed as a [kaggle kernel](https://www.kaggle.com/babinu/gradient-boosting-add-item-category-average?scriptVersionId=21090751) to improve running speed.

## Important note regarding creation of training and validation sets

As illustrated in the [following kaggle kernel](https://www.kaggle.com/dlarionov/feature-engineering-xgboost), performance of  models really improve if trained data is augmented by adding entries for all combinations of shop_id, item_id for a particular month (that is if the data has 2 shop_id's and 2 item_id's for a particular month, but has a non zero entry for only 1 shop_id, item_id combination(amongst the four), zero entries for the other 3 shop_id, item_id combinations can be appended to the data). Once, the data set is enlarged in this manner and the data for the last month is set as the validation set, and the data corresponding to the previous months as the training set, we see that the model trains and performs pretty well.

The sections below describes how different modeling techniques performed on this new enlarged data set.

### Gradient boosting on new dataset 
This has been implemented in [xgboost_final_full_features.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/more_complex_models/xgboost_final_full_features.ipynb). The validation error reduces to around 0.917

### DNN on new dataset
This has been implemented in [dnn_tensorflow.ipynb](https://github.com/babinu-uthup-4JESUS/Kaggle-Predict-Future-Sales/blob/master/dnn_tensorflow.ipynb).  The validation error came out to be around 1.15.

## Final Conclusion
To conclude, the major breakthrough in this project, was not any particular modeling technique, but rather the enlargement of dataset to include more shop_id, item_id combinations. Once the dataset was enlarged in this manner, a gradient boosting model with appropriate features trained over the same produced the best results with a validation error of 0.917 and a test set error of approximately 0.973.
