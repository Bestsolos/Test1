## accuracy
import numpy as np
from sklearn.metrics import accuracy_score

y_pred = [0, 1, 0, 1]
y_true = [0, 1, 1, 1]

print('ACC:',accuracy_score(y_true, y_pred))