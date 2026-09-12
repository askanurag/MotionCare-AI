# Raw Signal Workflow

Raw IMU sessions now connect to an actual feature-extraction and training workflow. Each session CSV has timestamp seconds, six axis columns, a synthetic patient identity and point-event markers. Load sessions, extract windows, group-split patients, train, select threshold on validation, then evaluate held-out patients. The original Gaussian tabular demo remains a separate experiment.
