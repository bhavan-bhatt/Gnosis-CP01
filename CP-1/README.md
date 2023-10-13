# T15: Gnosis-CP01
## **Course Project - 01: Data Preprocessing, EDA and Regression Analysis**

### **Dataset3: CDC Dataset**

### **Submitted By: T15-Gnosis**

- Bhavan Bhatt(202311021)
- Pratham Patel(202311022)
- Harshneel Soni(202311024)
- Nishit Munjani(202311026)
- Rohit Rathod(202311039)

**Introduction to the data and problem we are trying to solve:**

The dataset we have is Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System provided by Centers for Diseass control and prevention(CDC).This dataset includes data on adult's diet, physical activity, and weight status from Behavioral Risk Factor Surveillance System. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, and physical activity. [Here](https://www.kaggle.com/datasets/spittman1248/cdc-data-nutrition-physical-activity-obesity) is the reference link to the same.

It covers mainly 3 topics:

1. Obesity
2. Fruits and Vegetables
3. Physical Activity

Out of these looking at the current trends we are focusing on the Obesity, which covers two questions, "Percent of adults aged 18 years and older who have obesity" & "Percent of adults aged 18 years and older who have an overweight classification". We will be treating this as our primary problem to solve.

We tried to check the correlation of Income and Education as well as other features and observed their relationship with Obseity in United States of America. Before going on to predict we did a bit of data cleaning and interpreted some of the statistics mentioned in the dataset. We also did feature engineering to change the scale of some features and then train the model accordingly. We made regression model using different algorithms such as Linear Regression, Ridge Regression,Stochastic Gradient Descent Regressor, Random Forest Regressor as well as Xgboost regression. We also tried to tune the hyperparameters of some of these models, and at last compared the results of these models on the basis of standard metrics such as MAE,RMSE and R2-score.
