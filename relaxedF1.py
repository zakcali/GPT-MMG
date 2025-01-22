import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, cohen_kappa_score

# Read the CSV file
df = pd.read_csv("entities_f1.csv", sep=";")

# Extract the y_predict and y_true columns as arrays
y_pred = df["y_pred"].values
y_true = df["y_true"].values

# Calculate overall Cohen's Kappa
overall_kappa = cohen_kappa_score(y_true, y_pred)

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)
labels = sorted(set(y_true))

# Calculate TP, FP, FN, TN for each class
TP = np.diag(cm)
FP = cm.sum(axis=0) - TP
FN = cm.sum(axis=1) - TP
TN = cm.sum() - (FP + FN + TP)

# Calculate per-label Cohen's Kappa
kappa_per_label = {}
for label in labels:
    y_true_binary = np.where(y_true == label, 1, 0)
    y_pred_binary = np.where(y_pred == label, 1, 0)
    kappa = cohen_kappa_score(y_true_binary, y_pred_binary)
    kappa_per_label[label] = kappa

# Prepare the header
header = f"Tr\\Pr\t" + "\t".join(labels) + "\tTP\tFP\tFN\tTN\tKappa\n"

# Prepare rows with confusion matrix data and statistics
rows = []
for i, label in enumerate(labels):
    row = [label] + cm[i].tolist() + [TP[i], FP[i], FN[i], TN[i], f"{kappa_per_label[label]:.4f}"]
    rows.append("\t".join(map(str, row)))

# Combine all output into the final report
report = (f"Output Report\n"
          f"========================\n\n"
          f"y_pred: {y_pred.tolist()}\n"
          f"y_true: {y_true.tolist()}\n\n"
          f"{classification_report(y_true, y_pred)}\n"
          f"Overall Cohen's Kappa: {overall_kappa:.4f}\n\n"
          f"Per-Label Cohen's Kappa:\n")
for label, kappa in kappa_per_label.items():
    report += f"  {label}: {kappa:.4f}\n"
report += "\n" + header + "\n".join(rows)

# Save the report to the file
with open("metrics_report.txt", "w") as file:
    file.write(report)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('confusion_matrix.png')
plt.close()  # Close the plot to prevent it from being displayed
print("Confusion matrix graphic saved as confusion_matrix.png, and metrics report saved as metrics_report.txt")
