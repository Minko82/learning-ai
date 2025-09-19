"""
📊 Logistic Regression & Employee Attrition Analysis

This script uses pandas, seaborn, matplotlib, and scikit-learn to analyze HR data related to employee attrition.
Key tasks include:
- Data preprocessing
- Visualization of feature distributions
- Logistic Regression modeling
- Model evaluation (confusion matrix, accuracy, etc.)

Dataset: HR_comma_sep.csv
"""

#!/usr/bin/env python
# coding: utf-8

# This dataset contains information about different attributes of employees from a company. There are 14999 employees records and 10 feature columns.  The columns are:
# 
#     satisfaction_level: Employee satisfaction score (1-5 scale).
#     last_evaluation: Score on last evaluation (1-5 scale).
#     number_project: Number of projects employee worked on.
#     average_monthly_hours: Average hours worked in a month.
#     time_spend_company: Number of years spent with the company.
#     work_accident: If an employee had a workplace accident (yes/no).
#     left: If an employee has left the company (yes/no).
#     promotion_last_5years: Number of promotions in last 5 years.
#     Department: Department of the employee.
#     Salary: Annual salary of employee.
# 



# Load libraries needed
# Run this in your terminal if you don't have these libraries:
# pip install pandas numpy matplotlib seaborn scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score
import matplotlib.pyplot as plt




# Read in the data
import os

# Load CSV from script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "HR_comma_sep.csv")
hr = pd.read_csv(file_path)



# Print the first 10 lines of the dataset for verification
hr.head(10)


#                             
# ```python
# hr['position'] = hr['sales'].map({'sales':1,'technical':2,'support':3,'IT':3,
#                                   'product_mng':1,'marketing':1,'RandD':2,
#                                   'accounting':3,'hr':3,'management':3})
# ```



# Just checking
hr.describe()




hr['position'] = hr['sales'].map({'sales':1,'technical':2,'support':3})

hr['salary'] = hr['salary'].map({'low':1, 'medium':2, 'high': 3})

hr = hr.drop('sales', axis=1)

# Had to drop NaN values because the position field had some null values which
# raised some errors
hr = hr.dropna()




# Just checking
hr.describe()


# Create a datsets for training and another for testing by randomly selecting 80% of the data for training and 20% for testing.  Call your datasets X_train, y_train, X_test, y_test

X = hr.drop('left', axis=1)
y = hr['left']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)



plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=list(X.columns), class_names=['Stay', 'Left'])
plt.show()



accuracy = clf.score(X_test, y_test)
print(f'Accuracy: {accuracy}')

cv_scores = cross_val_score(clf, X, y, cv=2)
print(f'2-way Cross-Validation Accuracy: {cv_scores.mean()}')



pruned_clf = DecisionTreeClassifier(max_depth=3)
pruned_clf.fit(X_train, y_train)



pruned_accuracy = pruned_clf.score(X_test, y_test)
print(f'3-Depth Accuracy: {pruned_accuracy}')

pruned_cv_scores = cross_val_score(pruned_clf, X, y, cv=2)
print(f'3-Depth 2-way Cross-Validation Accuracy: {pruned_cv_scores.mean()}')




plt.figure(figsize=(12, 8))
plot_tree(pruned_clf, filled=True, feature_names=list(X.columns), class_names=['Stay', 'Left'])
plt.show()



# ```python
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.model_selection import train_test_split, cross_val_score
# import matplotlib.pyplot as plt
# ```
# 
# 
# ```python
# df['Income'] = df['Income'].map({'50K': 1, '60K': 2, '45K': 3, '80K': 4, '55K': 5, '90K': 6, '65K': 7, '40K': 8, '70K': 9})
# ```
# 
# 
# ```python
# X = df.drop('BuysComputer', axis=1)
# y = df['BuysComputer']
# ```
# 
# 
# ```python
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# ```
# 
# 
# ```python
# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)
# ```
# 
# 
# ```python
# accuracy = clf.score(X_test, y_test)
# print(f'Accuracy: {accuracy}')
# ```
# 
# 
# ```python
# cv_scores = cross_val_score(clf, X, y, cv=2)
# print(f'2-way Cross-Validation Accuracy: {cv_scores.mean()}')
# ```
# 
# 
# ```python
# pruned_clf = DecisionTreeClassifier(max_depth=4)
# pruned_clf.fit(X_train, y_train)
# ```
# 
# 
# ```python
# pruned_accuracy = pruned_clf.score(X_test, y_test)
# print(f'Pruned Model Accuracy: {pruned_accuracy}')
# ```
# 
# 
# ```python
# plt.figure(figsize=(12, 8))
# plot_tree(pruned_clf, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])
# plt.show()
# ```