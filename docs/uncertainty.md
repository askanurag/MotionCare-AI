# Uncertainty

The bootstrap utility resamples rows and skips samples containing one class. Its 2.5 and 97.5 percentiles describe conditional sampling uncertainty. Use only one row per patient, or replace with cluster bootstrap. It does not account for model-selection uncertainty or dataset shift.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
