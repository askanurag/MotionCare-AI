# Data contract

Use the exact ordered feature names in `data/schema.json`, a string patient_id and a binary target. Inference omits the target. Numeric feature NaNs are accepted when each feature has some observations; infinity and entirely missing features are rejected. Outcomes, identifiers and post-outcome fields are never used as inputs.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
