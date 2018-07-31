## Linear Regression in R: 
```R
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

r, the correlation coefficient, represents the strength of the linear relationship between x and y [(2)](https://onlinecourses.science.psu.edu/stat501/node/256/). Does it tell us how closely related two variables are? No. An r of 0 means that two variables are not linearly correlated (there is no linear relationship). Negative r tells us that as one variable gets big the other gets small, and positive r says that both variables get bigger together.

A relationship may still exist if r is 0, but be perfect quadratic or distorted by outliers. Diagnostics of the residuals can ensure the validity of the linear form and is a mandatory process for every kind of statistical modeling.

Correlation does not imply causation. A common example of this: ice cream sales and murder rates were once found to be correlated, this does not imply that ice cream sales and rate of murder are related or that one caused the other.

This is only really helpful if X and y are linearly related quantitative variables - again, not just related. We can see that if there is no correlation between X and y then r ~0, slope ~0, and the prediction of y can only be assumed to be mean(y). This is why we check for one of the major assumptions of linear regression model: independence of the error.

Regression models are used for description, causal inference, or prediction y based on the relationship between X and y. Each of these uses depends on the model selection process. 

---

### BreakDown with References

   * r quantifies the strength of a linear relationship [(1)](https://onlinecourses.science.psu.edu/stat501/node/258/), not just that there is a relationship.

A regression line allows us to predict y based on the relationship between X and y. 
Two common definitions of "prediction":

   1. "Predict the output value (Y) for new observations given their input values (X)" [(4)](https://www.stat.berkeley.edu/~aldous/157/Papers/shmueli.pdf)

   2. "When the time of interest occurs after the last available
measurement" [3](http://d1.amobbs.com/bbs_upload782111/files_40/ourdev_647440XLQQDR.pdf)


    * Prediction vs Determination?
    * Extrapolation v Interpolation v "Prediction"


### Additional References
[Introduction to Linear Regression Analysis](https://media.wiley.com/product_data/excerpt/10/04705428/0470542810-66.pdf)

[An Introduction to Statistical Inference and Its Applications](https://shyam.nitk.ac.in/Books/PTA%20Books/Trosset-ProbTheory-n-statistical_inference.pdf)


## Linear Regression By Gradient Descent

* Learning rate - small = slow convergece, large = might not converge

Define converge 


