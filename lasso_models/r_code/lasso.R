# Apply lasso on the train set and see how it performs on the test set.

# Required input constants
PROJECT_DIR = "/Users/babs4JESUS/Documents/GitHub/Kaggle_Santander_Value_Prediction_Challenge/"
INPUT_DIR = paste(PROJECT_DIR, 'input/', sep = '')
LASSO_MODELS_DIR = paste(PROJECT_DIR, 'lasso_models/', sep = '')
PROJECT_R_CODE_DIRECTORY = paste(LASSO_MODELS_DIR, 'r_code/', sep = '')

# Read the train data
train = read.csv(file=paste(INPUT_DIR, "train.csv", sep=''),
                 header = TRUE,
                 sep = ",")

# Seprate into X and Y variables.
Y = data.matrix(train$target)
X = data.matrix(subset(train, select = -c(ID,target)))

# Apply lasso and inspect the output
library(glmnet)
glmnetout = glmnet(X, Y)

# Find the optimal value of lasso parameter lambda by cross validation.
holdcvout = cv.glmnet(X, Y)

# Let our eyes see what it has to offer !
plot(holdcvout)

# From the plot, we have the following information (which is derived below for more clarity as well)

# (lambda, # of parameters)  that is the minima is (484928.1, 48)
index_min = which(holdcvout$cvm == min(holdcvout$cvm), arr.ind = TRUE)
min_cv_num_param = holdcvout$nzero[index_min]
min_cv_lambda = holdcvout$lambda.min
stopifnot(min_cv_lambda == holdcvout$lambda[index_min])

# (lambda, # of parameters)  that is within 1 standard deviation to the minima 
# and which is used as per standard practice (1288012, 14)
one_se_lambda = holdcvout$lambda.1se
index_one_se_lambda = which(holdcvout$lambda == one_se_lambda, arr.ind = TRUE)
one_se_num_param = holdcvout$nzero[index_one_se_lambda]

# Let us build models based on these lambdas
glmouts = glmnet(X, Y, lambda = c(min_cv_lambda, one_se_lambda))

# Betas for the first model, that is the one corresponding to minimum cv score.
glmouts$beta[(glmouts$beta[,1]!=0),1]

# Betas for the second model, that is the one corresponding to 1 se cv score.
glmouts$beta[(glmouts$beta[,2]!=0),2]

# We would like to play around with these models, but let us do it in python. Hence let us
# write these models to csv files, from which we can export to python for further analysis.
write.csv(glmouts$beta[(glmouts$beta[,1]!=0),1] ,
          paste(LASSO_MODELS_DIR, 'minimum_cv_lasso_model_columns_and_coefficients.csv', sep = ''))

write.csv(glmouts$beta[(glmouts$beta[,2]!=0),2] ,
          paste(LASSO_MODELS_DIR, 'one_se_cv_lasso_model_columns_and_coefficients.csv', sep = ''))
