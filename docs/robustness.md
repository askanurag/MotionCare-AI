# Robustness

Missingness stress tests replace a seeded random fraction of numeric measurements with NaN. The fitted imputer handles these values. This mechanism is missing completely at random and cannot establish robustness to clinically structured missingness.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
