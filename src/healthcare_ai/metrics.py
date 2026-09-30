from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss, confusion_matrix, balanced_accuracy_score
def evaluate(y, probability, threshold=.5):
    prediction = probability >= threshold
    tn, fp, fn, tp = confusion_matrix(y, prediction, labels=[0,1]).ravel()
    both = len(set(y)) == 2
    return {'auroc': float(roc_auc_score(y, probability)) if both else None,
      'average_precision': float(average_precision_score(y, probability)) if both else None,
      'brier': float(brier_score_loss(y, probability)), 'balanced_accuracy': float(balanced_accuracy_score(y, prediction)),
      'sensitivity': float(tp/(tp+fn)) if tp+fn else None,
      'specificity': float(tn/(tn+fp)) if tn+fp else None,
      'tp':int(tp),'tn':int(tn),'fp':int(fp),'fn':int(fn),'n':len(y),'threshold':float(threshold)}
