import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the dog diseases dataset
df = pd.read_csv("dataset.csv")

# Define the input features (symptoms) and target variables (severity and treatment)
symptoms = df.columns[1:-2]
severity = df['Severity']
disease = df['Disease name']


# Split the dataset into training and testing sets
X_train, X_test, y_sev_train, y_sev_test, y_dis_train, y_dis_test = train_test_split(df[symptoms], severity, disease, test_size=0.2, random_state=42)

# Train decision tree models for severity and treatment prediction
sev_tree = DecisionTreeClassifier()
sev_tree.fit(X_train.values, y_sev_train)

dis_tree = DecisionTreeClassifier()
dis_tree.fit(X_train.values, y_dis_train)

# Make predictions on the test set
y_sev_pred = sev_tree.predict(X_test.values)
y_dis_pred = dis_tree.predict(X_test.values)

# Evaluate the accuracy of the models
sev_accuracy = accuracy_score(y_sev_test, y_sev_pred)
dis_accuracy = accuracy_score(y_dis_test, y_dis_pred)

print("Severity prediction accuracy:", sev_accuracy)
print("Disease prediction accuracy:", dis_accuracy)

# Save the trained models to disk
joblib.dump(sev_tree, "severity_model.joblib")
joblib.dump(dis_tree, "treatment_model.joblib")