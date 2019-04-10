# columbiaX-edX-a1
Machine Learning Assignment 1 in Python.

Type: Supervised learning, Regression.
Algos: Ridge Regression and Active Learning Procedure.

In ridge regression we add a penalization term to the OLS/MLE regression with lambda*||w||^2 term.
Lambda values that are too high will drive the weights of the regression to zero.
The motivation behind ridge regression is that the OLS/MLE might be overfitting the data
to noise and therefore will have a poor out-of-sample prediction accuracy. By choosing the
appropriate lambda the ridge regression will lower the magnitude of the weights and 
thus a lower forecasting variance: A bias-variance trade off. An analytic solution
exists to the ridge regression problem and doesn't require any optimization algorithms.
Ridge regression and the solution to the Maximum A Posteriori (MAP Regression) are the same. 
MAP looks for the set of weights that arg maximizes ln(w|y,X) while MLE looks for the set of weights
that arg maximizes ln(y|mu=Xw,sigma^2).

![alt text](https://github.com/frogger21/columbiaX-edX-a1/blob/master/edx1.JPG)

source: Professor John Paisley's ML lecture at ColumbiaX edX.

Lasso regressions are motiviated similarly to the ridge regression except that it adds a
lambda*||w|| term. While ridge penalizes high magnitude weights with priority, Lasso does not
care if the weights are small or big, they will equally get penalized. Lasso is useful if the number
of features of X are greater than the observations in the data (can't even run OLS/MLE). 
Lasso will drive certain weights to 0.

![alt text](https://github.com/frogger21/columbiaX-edX-a1/blob/master/edx2.JPG)

source: Professor John Paisley's ML lecture at ColumbiaX edX.



