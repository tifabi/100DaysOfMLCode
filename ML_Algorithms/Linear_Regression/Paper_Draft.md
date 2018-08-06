

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

__R-squared__

One of the most common metric when evaluating linear regression models is the R-squared value, or put more scarily, "the coefficient of determination." The R-squared value captures how well our model does at explaining the variance seen in the dependent variable (y) using our independent variable (x). The higher the R-squared value the better our model does at explaining our observations. First, we'll present some scary math and then explain what it means. Formally, here's how one calculates R-squared:

<a href="https://www.codecogs.com/eqnedit.php?latex=SS_{tot}=\sum&space;_i(y_i-\bar&space;y)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SS_{tot}=\sum&space;_i(y_i-\bar&space;y)^2" title="SS_{tot}=\sum _i(y_i-\bar y)^2" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=SS_{res}=\sum&space;_i(y_i-f(x_i))^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SS_{res}=\sum&space;_i(y_i-f(x_i))^2" title="SS_{res}=\sum _i(y_i-f(x_i))^2" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=R^2=1-\frac{SS_{res}}{SS_{tot}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^2=1-\frac{SS_{res}}{SS_{tot}}" title="R^2=1-\frac{SS_{res}}{SS_{tot}}" /></a>

While complex looking, the equation can be easily broken down into 1 or 2 lines of Python. Continuing from our previous example where we had calculated our model's slope and intercept, we can calculate our RSQ as:

```R
# In R:
yhat = x * slope + intercept
rsq = sum((yhat - mean(x))^2)/sum((x - mean(x))^2)
```
And it's as simple as that! The resulting number will be bounded betwen [0, 1] with 0 denoting no gain in accuracy (our model has no good explanation for our data) and a 1 denoting perfect accuracy (our model is always, exactly right). The next, natural, and most common question then follows: how high an R-squared value is 'good enough'? While, as always, we want our model to be as accurate as possible, we cannot always hope for perfection (R-squared=1.00). Typically, models begin to perform pretty well with R-squared values above 0.3-0.4 and become better as more data is added.

It is important, however, to note that care has to be taken when evaluating the R-squared score. Often, people will get stuck 'chasing R' and endlessly tweak their model trying to wring a higher score out of it. What happens, though, is that more-and-more variables get included in the model, the R score improves, and development ends when the score has reached some arbitrary value (e.g. 0.90). The model is deployed and what happens? It fails miserably as it's now 'overfitted' to the data and lacks the ability to generalize. This leads to one of the key takeaways when discussing R-squared: adding data to the model, even if it is random noise, will always improve R-squared to some degree. Always ask yourself: does this data make sense given what I'm trying to model?

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
