import ast
import spacy
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the spaCy model
nlp = spacy.load("model-best")

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return ast.literal_eval(content)

def parse_entities(data, nlp):
    true_entities = []
    pred_entities = []
    
    for text, annotations in data:
        true_ents = annotations['entities']
        
        # Get predictions from the loaded model
        doc = nlp(text)
        pred_ents = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
        
        # Ensure we have a prediction for each true entity
        for start, end, label in true_ents:
            true_entities.append(label)
            pred_label = next((ent[2] for ent in pred_ents if ent[0] == start and ent[1] == end), 'O')
            pred_entities.append(pred_label)
    
    return true_entities, pred_entities

def plot_confusion_matrix(y_true, y_pred, labels):
    # Filter out "O" labels
    y_true_filtered = [y for y in y_true if y != 'O']
    y_pred_filtered = [y_pred[i] for i, y in enumerate(y_true) if y != 'O']
    labels_filtered = [label for label in labels if label != 'O']

    cm = confusion_matrix(y_true_filtered, y_pred_filtered, labels=labels_filtered)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels_filtered, yticklabels=labels_filtered)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    plt.close()
    return cm, labels_filtered

def generate_confusion_matrix_report(cm, labels):
    report = "Confusion Matrix Report\n"
    report += "=============================================\n\n"
    
    # Header
    report += "Tr\\Pr\t" + "\t".join(labels) + "\tTP\tFP\tFN\tTN\n"
    
    n_classes = len(labels)
    
    for i, true_label in enumerate(labels):
        row = [str(cm[i, j]) for j in range(n_classes)]
        tp = cm[i, i]
        fp = np.sum(cm[:, i]) - tp
        fn = np.sum(cm[i, :]) - tp
        tn = np.sum(cm) - tp - fp - fn
        
        report += f"{true_label}\t" + "\t".join(row) + f"\t{tp}\t{fp}\t{fn}\t{tn}\n"
    
    return report

def generate_report(y_true, y_pred, labels):
    report = "Entity Recognition Report\n"
    report += "==========================\n\n"
    
    # Filter out "O" labels
    y_true_filtered = [y for y in y_true if y != 'O']
    y_pred_filtered = [y_pred[i] for i, y in enumerate(y_true) if y != 'O']
    labels_filtered = [label for label in labels if label != 'O']
    
    # Calculate overall accuracy
    accuracy = accuracy_score(y_true_filtered, y_pred_filtered)
    report += f"Overall Accuracy: {accuracy:.4f}\n\n"
    
    # Calculate precision, recall, and F1-score for each label
    precision, recall, f1, support = precision_recall_fscore_support(y_true_filtered, y_pred_filtered, labels=labels_filtered, zero_division=0)
    
    # Calculate macro and weighted averages
    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(y_true_filtered, y_pred_filtered, labels=labels_filtered, average='macro', zero_division=0)
    weighted_precision, weighted_recall, weighted_f1, _ = precision_recall_fscore_support(y_true_filtered, y_pred_filtered, labels=labels_filtered, average='weighted', zero_division=0)
    
    # Add macro and weighted averages to the report
    report += "Macro Average:\n"
    report += f"  Precision: {macro_precision:.4f}\n"
    report += f"  Recall: {macro_recall:.4f}\n"
    report += f"  F1-score: {macro_f1:.4f}\n\n"
    
    report += "Weighted Average:\n"
    report += f"  Precision: {weighted_precision:.4f}\n"
    report += f"  Recall: {weighted_recall:.4f}\n"
    report += f"  F1-score: {weighted_f1:.4f}\n\n"
    
    report += "Individual Labels:\n"
    for i, label in enumerate(labels_filtered):
        report += f"{label}:\n"
        report += f"  Precision: {precision[i]:.4f}\n"
        report += f"  Recall: {recall[i]:.4f}\n"
        report += f"  F1-score: {f1[i]:.4f}\n"
        report += f"  Support: {support[i]}\n\n"
    
    return report

# Load the data
data = load_data('test.json')

# Parse entities using the loaded model
true_entities, pred_entities = parse_entities(data, nlp)

print(f"Number of true entities: {len(true_entities)}")
print(f"Number of predicted entities: {len(pred_entities)}")

# Get unique labels
labels = sorted(set(true_entities + pred_entities))

# Plot confusion matrix and get the matrix (excluding "O" label)
cm, labels_filtered = plot_confusion_matrix(true_entities, pred_entities, labels)

# Generate confusion matrix report
cm_report = generate_confusion_matrix_report(cm, labels_filtered)

# Generate entity recognition report
er_report = generate_report(true_entities, pred_entities, labels)

# Save confusion matrix report to TXT file
with open('confusion_matrix_report.txt', 'w', encoding='utf-8') as f:
    f.write(cm_report)

# Save entity recognition report to TXT file
with open('entity_recognition_report.txt', 'w', encoding='utf-8') as f:
    f.write(er_report)

print("Confusion matrix saved as 'confusion_matrix.png'")
print("Confusion matrix report saved as 'confusion_matrix_report.txt'")
print("Entity recognition report saved as 'entity_recognition_report.txt'")