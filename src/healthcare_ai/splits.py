from sklearn.model_selection import GroupShuffleSplit
def split(frame, seed=42):
    splitter = GroupShuffleSplit(n_splits=1, test_size=.2, random_state=seed)
    trainval, test = next(splitter.split(frame, groups=frame.patient_id))
    pool = frame.iloc[trainval]
    inner = GroupShuffleSplit(n_splits=1, test_size=.25, random_state=seed+1)
    train, val = next(inner.split(pool, groups=pool.patient_id))
    return pool.iloc[train].copy(), pool.iloc[val].copy(), frame.iloc[test].copy()
