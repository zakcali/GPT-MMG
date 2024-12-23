def get_ner_prf(examples: Iterable[Example], **kwargs) -> Dict[str, Any]:
    """Compute micro-PRF, per-entity PRF scores, overall accuracy, and overall support."""
    score_per_type = defaultdict(PRFScore)
    total_tp, total_fp, total_fn = 0, 0, 0  # Initialize overall counts for accuracy and support calculation

    for eg in examples:
        if not eg.y.has_annotation("ENT_IOB"):
            continue
        golds = {(e.label_, e.start, e.end) for e in eg.y.ents}
        align_x2y = eg.alignment.x2y
        for pred_ent in eg.x.ents:
            if pred_ent.label_ not in score_per_type:
                score_per_type[pred_ent.label_] = PRFScore()
            indices = align_x2y[pred_ent.start : pred_ent.end]
            if len(indices):
                g_span = eg.y[indices[0] : indices[-1] + 1]
                # Check we aren't missing annotation on this span. If so,
                # our prediction is neither right nor wrong, we just ignore it.
                if all(token.ent_iob != 0 for token in g_span):
                    key = (pred_ent.label_, indices[0], indices[-1] + 1)
                    if key in golds:
                        score_per_type[pred_ent.label_].tp += 1
                        total_tp += 1  # Update total TP
                        golds.remove(key)
                    else:
                        score_per_type[pred_ent.label_].fp += 1
                        total_fp += 1  # Update total FP
        for label, start, end in golds:
            score_per_type[label].fn += 1
            total_fn += 1  # Update total FN

    totals = PRFScore()
    for prf in score_per_type.values():
        totals += prf

    # Calculate overall accuracy
    total_predictions = total_tp + total_fp + total_fn
    overall_accuracy = total_tp / total_predictions if total_predictions > 0 else None

    # Calculate overall support
    overall_support = total_tp + total_fn  # Total TP + FN is the overall support

    if len(totals) > 0:
        return {
            "ents_p": totals.precision,
            "ents_r": totals.recall,
            "ents_f": totals.fscore,
            "ents_acc": overall_accuracy,  # Include overall accuracy
            "ents_support": overall_support,  # Include overall support
            "ents_per_type": {
                k: {
                    "p": v.precision,
                    "r": v.recall,
                    "f": v.fscore,
                    "tp": v.tp,
                    "fp": v.fp,
                    "fn": v.fn,
                    "support": v.tp + v.fn,
                }
                for k, v in score_per_type.items()
            },
        }
    else:
        return {
            "ents_p": None,
            "ents_r": None,
            "ents_f": None,
            "ents_acc": None,
            "ents_support": None,
            "ents_per_type": None,
        }
