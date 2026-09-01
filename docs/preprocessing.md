# Preprocessing

Median imputation with missingness indicators and StandardScaler live inside the sklearn pipeline. Fitting occurs only on training data. Cross-validation creates fresh pipelines for each fold. No global imputation or normalization is performed.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
