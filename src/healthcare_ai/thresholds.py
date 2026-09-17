import numpy as np
from sklearn.metrics import balanced_accuracy_score
def select_threshold(y, p):
    grid = np.linspace(.1, .9, 81)
    scores = [balanced_accuracy_score(y, p >= t) for t in grid]
    return float(grid[int(np.argmax(scores))])
