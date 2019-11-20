import numpy as np
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
from sklearn import linear_model

def get_train_test_data(input_dir):
    train = pd.read_csv(input_dir + 'train.csv')
    test = pd.read_csv(input_dir + 'test.csv')
    train['log_target'] = np.log(train['target']) + 1.0
    return (train, test)

def get_train_data(input_dir):
    train = pd.read_csv(input_dir + 'train.csv')
    train['log_target'] = np.log(train['target']) + 1.0
    return train

def get_test_data(input_dir):
    test = pd.read_csv(input_dir + 'test.csv')
    return test

def get_all_predictor_cols(train):
    cols = [col for col in train.columns if col not in ['ID', 'target', 'log_target']]
    return cols

def evaluate_model_score(my_model, X, Y):
    predictions = my_model.predict(X)
    return evaluate_model_score_given_predictions(predictions, Y)

def make_predictions(my_model, X):
    predictions = my_model.predict(X)
    return predictions

def evaluate_model_score_given_predictions2(predictions, Y):
    mean_of_squared_error1 = \
        mean_squared_error((np.log(np.abs(Y + 1))), (np.log(np.abs(predictions + 1))))
    return np.sqrt(mean_of_squared_error1)

def evaluate_model_score_given_predictions(predictions, Y):
    mean_of_squared_error1 = \
        mean_squared_error(Y, predictions)
    return np.sqrt(mean_of_squared_error1)

def evaluate_neg_model_score(my_model, X, Y):
    return (-1) * evaluate_model_score(my_model, X, Y)


def cross_val_scores_given_model(my_model, X, Y, cv=5):
    cross_val_score1 = cross_val_score(my_model, 
                                       X, Y, 
                                       scoring=evaluate_model_score,
                                       cv=cv)
    return cross_val_score1

def cross_val_score_given_model(my_model, X, Y, cv=5):
    cross_val_score1 = cross_val_score(my_model, 
                                       X, Y,
                                       scoring=evaluate_model_score, 
                                       cv=cv)
                                       
    return cross_val_score1.mean()

def fit_pipeline_and_cross_validate(my_pipeline,
                                    train_data,
                                    X_columns,
                                    Y_column='log_target'):
    X = train_data[X_columns]
    Y = train_data[[Y_column]].values.ravel()
    my_pipeline.fit(X, Y)
    return (my_pipeline, cross_val_score_given_model(my_pipeline, X, Y))

def get_rel_cols(percent_threshold, data):
    cols_apart_from_id_and_target = [col for col in data.columns if col not in ['ID', 'target', 'log_target']]

    non_zero_percent_for_col = np.zeros(len(cols_apart_from_id_and_target))

    for i in range(len(cols_apart_from_id_and_target)):
        non_zero_percent_for_col[i] = \
            100.0* len(data[cols_apart_from_id_and_target[i]].to_numpy().nonzero()[0])/\
        len(data[cols_apart_from_id_and_target[i]].to_numpy())    

    num_rel_entries = np.sum(non_zero_percent_for_col > percent_threshold)

    rel_col_indices = np.argsort(non_zero_percent_for_col)[::-1][0:num_rel_entries]

    rel_cols = [cols_apart_from_id_and_target[col] for col in rel_col_indices]
    
    return rel_cols