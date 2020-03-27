## Precision,Recall,F1-score
from sklearn import metrics

y_pred = [0, 1, 0, 0]
y_true = [0, 1, 0, 1]

print('Precision',metrics.precision_score(y_true, y_pred))
print('Recall',metrics.recall_score(y_true, y_pred))
print('F1-score:',metrics.f1_score(y_true, y_pred))