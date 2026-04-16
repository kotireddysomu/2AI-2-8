# Cross Validation
cv_scores = cross_val_score(model, X, Y, cv=5)

print("Cross Validation Accuracy:", cv_scores.mean())

# Train model
model.fit(X_train, Y_train)

# Predictions
Y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("Classification Report:\n", classification_report(Y_test, Y_pred))

