# columbiaX-edX-a1
Machine Learning Assignment 1 in Python.

Type: Supervised learning, Regression.
Algos: Ridge Regression and Active Learning Procedure.

In ridge regression we add a penalization term to OLS/MLE regression with lambda*||w||^2 term.
Lambda values that are too high will drive the weights of the regression to zero.
The motivation behind ridge regression is that the OLS/MLE might be overfitting the data
to noise and therefore has a poor out-of-sample prediction accuracy. By choosing the
appropriate lambda the ridge regression will lower the magnitude of the weights and 
have a lower forecasting variance. A bias-variance trade off. 
