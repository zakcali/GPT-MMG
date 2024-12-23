import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_recall_fscore_support

# Read the CSV file
df = pd.read_csv("entities_f1.csv", sep=";")

# Extract the y_predict and y_true columns as arrays
y_pred = df["y_pred"].values
y_true = df["y_true"].values

# Print the arrays (optional)
print("y_pred:", y_pred)
print("y_true:", y_true)

# Generate and print the classification report
print(classification_report(y_true, y_pred))

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)
labels = sorted(set(y_true))

# Calculate TP, FP, FN, TN for each class
TP = np.diag(cm)
FP = cm.sum(axis=0) - TP
FN = cm.sum(axis=1) - TP
TN = cm.sum() - (FP + FN + TP)

# Prepare the header
header = f"Tr\\Pr\t" + "\t".join(labels) + "\tTP\tFP\tFN\tTN\n"

# Prepare rows with confusion matrix data and statistics
rows = []
for i, label in enumerate(labels):
    row = [label] + cm[i].tolist() + [TP[i], FP[i], FN[i], TN[i]]
    rows.append("\t".join(map(str, row)))

# Combine header and rows into the final report
report = "Confusion Matrix Report\n========================\n\n" + header + "\n".join(rows)

# Save confusion matrix report
with open("confusion_matrix_report.txt", "w") as file:
    file.write(report)

# Plot confusion matrix
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('confusion_matrix.png')
plt.show()
