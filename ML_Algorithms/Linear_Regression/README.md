# Purpose
While learning simple linear regression and having numerous discussions inside and outside of class, it became clear that there are many misconceptions, misunderstandings, and overall clarity needed to accurately apply and interpret simple linear regression. 
Since starting this mini-project, I have learned so much about simple linear regression from clarifying my understanding to interpreting applications. I wanted to extend this opportunity to collaborate and build a guide with others who are interested in building their own knowledge, joining a network excited about the possibilities, and creating a resource for both beginners and novices. 
# Timeline
Goal is to complete the bulk of work before the start of the Fall semester (Aug 20), peer review / revise / submission process would stretch over the Fall semester, and an overall target publication date by commencement day: Dec 15, 2018. 
# Outcome
Publish to a reputable website following peer review from at least one IU statistics professor.
# Overview
*	Create an easy-to-follow guide to demonstrate the modeling process for applying simple linear regression (Ordinary Least Squares- OLS). 
*	Highlight the entire process involved in modeling with linear regression: goal definition, study design, data collection, scientific use and interpretation. 
*	Make each definition easy and clear enough for a non-statistician to understand without oversimplifying (think explaining simple linear regression to Grandma). 
*	Address common misunderstanding or misinterpretations. 
# Project Description
Open to suggested format, but currently following a similar format to this paper: https://www.stat.berkeley.edu/~aldous/157/Papers/shmueli.pdf
1.	Define Simple Linear Regression 
  a.	Describe differences between Simple Linear Regression by OLS and other types of regression such as linear regression by gradient descent, time series. 
  b.	Identify and point out common misconceptions. This can come up through the process of oversimplifying, for example:
__Oversimplification:__ The correlation coefficient represents the relationship between x and y.
__Clarification:__ The correlation coefficient, represents the strength and direction (positive or negative) of the linear relationship between x and y.
  c.	Explore criticisms of using simple linear regression for the different modeling techniques, for example:
  Should simple linear regression be used for prediction, why or why not?
  Can R-square be negative? Many say it can, but many say it can’t.
  d.	Draft description here: https://github.com/tifabi/100DaysOfMLCode/tree/master/ML_Algorithms/Linear_Regression 
2.	Define Modeling and what types of modeling linear regression can be used for (explanatory, predictive, descriptive).
3.	Define assumptions and provide some methods for checking assumptions using python and R. 
4.	Provide clear examples for calculating simple linear regression in python and R. This is already done in R, and partially in python (need to add notes and the use of packages to calculate), example of calculating in python here: https://github.com/tifabi/100DaysOfMLCode/blob/master/ML_Algorithms/Linear_Regression/Simple_LinearRegression.ipynb
5.	Explore some examples from journal articles / published peer reviewed experiments applying simple linear regression.
# Potential Areas of Contribution
1.	Working on definitions, examples include:
  1.	Describing explanatory modeling in detail
  2.	Defining R-square simple enough for the non-statistician
2.	Straightforward code with easy-to-follow comments in python and R, other languages could be included to demonstrate calculations from scratch and available packages/libraries. A comparison of simple linear regression coded in various languages could be an addition, but the minimum will be python and R. 
  1.	Calculating simple linear regression
  2.	Checking assumptions
3.	Exploring published uses to provide examples of application and interpretation.




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


