from sklearn.pipeline import Pipeline
from .models import classifier
from .preprocessing import preprocessing
def build(name='logistic', seed=42):
    return Pipeline([('preprocess', preprocessing()), ('model', classifier(name, seed))])
