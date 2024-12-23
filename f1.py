import pandas as pd
from sklearn.metrics import classification_report

# Read the CSV file
df = pd.read_csv("entities_f1.csv", sep=";")

# Extract the y_predict and y_true columns as arrays
y_pred = df["y_pred"].values
y_true = df["y_true"].values

# Print the arrays (optional)
print("y_pred:", y_pred)
print("y_true:", y_true)

print(classification_report(y_true, y_pred))