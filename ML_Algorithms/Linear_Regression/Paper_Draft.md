

Simple Linear Regression is __INSERT DEFINITION__. It is useful for __INSERT USES__. A simple linear regression line can be calculated in R as seen in R code below:

```R
# In R:

X <- c(2,3,4,3,2,9,6,7,2,9)
y <- c(12,54,23,45,23,12,34,23,55,23)
r = cor(X, y)
slope = r * sd(y) / sd(X)
intercept = mean(y) - slope * mean(X)
intercept + slope * 5

> [1] 29.65187

OR with lm:
mod = lm(y~X)
predict(mod, X <- 5)

> 1 
> 29.65187
```

r, The correlation coefficient, represents the strength and direction (positive or negative) of the linear relationship between x and y. [(2)](https://onlinecourses.science.psu.edu/stat501/node/256/). Does it tell us how closely related two variables are? No. An r of 0 means that there is no linear relationship between two variables (the are not linearly correlated). Negative r tells us that as one set of variables get big the other set tends gets small, and positive r says that both sets tend to get bigger together. This describes the trend, not specific points.

Code section # shows how r can be calculated from scratch in Python.

```Python
# In Python:
r = ((n * sum([i*y[z] for z, i in enumerate(X)]) - (sum(X) * sum(y)))
         / ((n * sum([i**2 for i in X]) - sum(X)**2) * (n * sum([i**2 for i in y]) - sum(y)**2))**0.5)
```

A relationship may still exist if r is 0, but be perfect quadratic or distorted by outliers. Diagnostics of the residuals can ensure the validity of the linear form and is a mandatory process for every kind of statistical modeling.

Correlation does not imply causation. A common example of this: ice cream sales and murder rates were once found to be correlated, this does not imply that ice cream sales and rate of murder are related or that one caused the other.

__INSERT R-squared definition__

__INSERT definition of slope__

Code section # shows how slope can be calculated from scratch in Python using the r defined in code section #.

```Python
# In Python:
def mean(numList):
    return float(sum(numList)) / len(numList) if len(numList) > 0 else 0

def sd(numList):
    meanList = mean(numList)
    return float(((sum([(i - meanList)**2 for i in numList])) 
                 / (len(numList) - 1))**0.5)

slope = r * (sd(y) / sd(X))
```

Simple Linear Regression is only really helpful if X and y are linearly related quantitative __DEFINE "quantitative"__ variables - again, not just related. We can see that if there is no correlation between X and y then r ~0, slope ~0, and the prediction of y can only be assumed to be mean(y). This is why we check for one of the major assumptions of the linear regression model: linearity.

__INSERT Definition of linearity__

__INSERT Definition Independence of errors & define the error__

__INSERT Definition Homoskedasticity__

__INSERT Definition Normality of errors & define the error__


Regression models are used for description, causal inference, or prediction y based on the relationship between X and y [(4)](https://www.stat.berkeley.edu/~aldous/157/Papers/shmueli.pdf). Each of these uses depends on the model selection process. __INSERT Defintions for Modeling__

__Compare Simple Linear Regression to other types - weighted, gradient descent__

__Include Example from literature__
