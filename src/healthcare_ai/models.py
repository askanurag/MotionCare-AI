from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, HistGradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
NAMES = ['logistic','random_forest','extra_trees','hist_gradient','naive_bayes','knn']
def classifier(name='logistic', seed=42):
    models = {'logistic': lambda: LogisticRegression(max_iter=500, random_state=seed),
      'random_forest': lambda: RandomForestClassifier(n_estimators=60, min_samples_leaf=4, random_state=seed, n_jobs=1),
      'extra_trees': lambda: ExtraTreesClassifier(n_estimators=60, min_samples_leaf=4, random_state=seed, n_jobs=1),
      'hist_gradient': lambda: HistGradientBoostingClassifier(max_iter=60, random_state=seed),
      'naive_bayes': GaussianNB, 'knn': lambda: KNeighborsClassifier(n_neighbors=15)}
    if name not in models: raise ValueError('Unknown model: '+name)
    return models[name]()
