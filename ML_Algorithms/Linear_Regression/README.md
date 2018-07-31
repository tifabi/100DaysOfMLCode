Linear Regression by Ordinary Least Squares in R: 
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

r is the correlation coefficient and represents the strength of the linear relationship between x and y [2](https://onlinecourses.science.psu.edu/stat501/node/256/)

An r of 0 means here that the two variables are not linearly correlated, 

    * Frequent Error: r quantifies the strength of a linear relationship [1](https://onlinecourses.science.psu.edu/stat501/node/258/)

negative r tells us that as one variable gets big the other gets small, and positive r says that both variables get bigger together. 

A regression line allows us to predict y based on the relationship between X and y. 
Two common definitions of "prediction":

   1. "Predict the output value (Y) for new observations given their input values (X)" [4](https://www.stat.berkeley.edu/~aldous/157/Papers/shmueli.pdf)

   2. "When the time of interest occurs after the last available
measurement" [3](http://d1.amobbs.com/bbs_upload782111/files_40/ourdev_647440XLQQDR.pdf)


    * Prediction vs Determination?


This is only really helpful if X and y are linearly related quantitative variables, 
    * Not just related


so we can see that if there is no correlation between X and y then r ~0, slope ~ 0, and the prediction of y can only be assumed to be mean(y). This is why we want to check for independence. 


### Additional References
[Introduction to Linear Regression Analysis](https://media.wiley.com/product_data/excerpt/10/04705428/0470542810-66.pdf)

[An Introduction to Statistical Inference and Its Applications](https://shyam.nitk.ac.in/Books/PTA%20Books/Trosset-ProbTheory-n-statistical_inference.pdf)

