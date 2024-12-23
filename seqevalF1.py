from seqeval.metrics import classification_report, accuracy_score, f1_score
from seqeval.scheme import IOB2

def evaluate_ner(true_file, pred_file):
    """
    Evaluates NER performance by comparing true and predicted BIO files using seqeval.

    Args:
        true_file: Path to the BIO file with true (gold standard) NER labels.
        pred_file: Path to the BIO file with predicted NER labels.

    Returns:
        A dictionary containing precision, recall, F1-score, and accuracy.
    """

    true_labels = []
    pred_labels = []

    with open(true_file, 'r', encoding='utf-8') as true_f, \
            open(pred_file, 'r', encoding='utf-8') as pred_f:

        true_sent = []
        pred_sent = []

        for true_line, pred_line in zip(true_f, pred_f):
            true_line = true_line.strip()
            pred_line = pred_line.strip()

            if not true_line:  # End of sentence
                true_labels.append(true_sent)
                pred_labels.append(pred_sent)
                true_sent = []
                pred_sent = []
            else:
                true_token, true_label = true_line.split('\t')
                pred_token, pred_label = pred_line.split('\t')
                true_sent.append(true_label)
                pred_sent.append(pred_label)

        if true_sent and pred_sent: # Handle the last sentence if no newline at the end
            true_labels.append(true_sent)
            pred_labels.append(pred_sent)

    report = classification_report(true_labels, pred_labels, mode='strict', scheme=IOB2)
    f1 = f1_score(true_labels, pred_labels, mode='strict', scheme=IOB2)
    accuracy = accuracy_score(true_labels, pred_labels)
    return report, f1, accuracy


# Example usage:
true_file = 'y_true.bio'
pred_file = 'y_pred.bio'

report, f1, accuracy = evaluate_ner(true_file, pred_file)

print(report)
print("F1 score:", f1)
print("Accuracy score:", accuracy)

