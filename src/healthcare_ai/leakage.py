def assert_disjoint(*frames):
    sets=[set(f.patient_id) for f in frames]
    for i,a in enumerate(sets):
        for b in sets[i+1:]:
            if a & b: raise ValueError('Patient leakage between partitions')
    return True
