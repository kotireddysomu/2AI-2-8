TEAM-8
LOGISTICS REGRESSION - ASSIGNMENT
Logistic Regression :-

📌 Introduction
Logistic Regression is a supervised machine learning algorithm used for classification problems, especially when the output is categorical (e.g., Yes/No, 0/1, True/False).
Unlike linear regression, it predicts the probability that a given input belongs to a particular class.

Why Not Linear Regression?
Linear regression gives continuous output (e.g., 45.6, 78.2)
Classification needs discrete output (0 or 1)
Logistic regression solves this by using a sigmoid function

📌 Sigmoid Function (Logistic Function)
�
Converts any real value into a range between 0 and 1
Output represents probability

📌 Model Representation
Logistic regression uses a linear equation:
Then applies sigmoid:

📌 Decision Boundary
If probability ≥ 0.5 → Class 1
If probability < 0.5 → Class 0
The boundary separating classes is called the decision boundary

📌 Types of Logistic Regression
Binary Logistic Regression
Two classes (0 or 1)
Multinomial Logistic Regression
More than two classes
Ordinal Logistic Regression
Ordered categories (e.g., low, medium, high)

📌 Cost Function (Loss Function)
Logistic regression uses Log Loss (Cross-Entropy Loss):
Penalizes wrong predictions heavily
Helps improve model accuracy

📌 Training the Model
Uses Gradient Descent to minimize loss
Updates weights iteratively

📌 Advantages
✔ Simple and easy to implement
✔ Works well for binary classification
✔ Outputs probabilities
✔ Efficient for large datasets

📌 Disadvantages
✖ Cannot handle complex relationships well
✖ Sensitive to outliers
✖ Assumes linear relationship between features and log-odds

📌 Applications
Email spam detection
Disease prediction
Credit risk analysis
Customer churn prediction

📌 Example
If predicting whether a student passes:
Input: Study hours
Output: Probability of passing
If output = 0.8 → Student likely passes


📌 Conclusion
Logistic Regression is a fundamental classification algorithm that uses probability and the sigmoid function to make predictions. It is widely used due to its simplicity and effectiveness.
