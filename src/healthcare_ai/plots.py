def plot_roc(y,p):
    import matplotlib.pyplot as plt
    from sklearn.metrics import RocCurveDisplay
    RocCurveDisplay.from_predictions(y,p);plt.title('Synthetic held-out ROC');return plt.gcf()
def plot_features(frame):
    from .settings import FEATURES
    return frame[FEATURES].hist(figsize=(10,6))
