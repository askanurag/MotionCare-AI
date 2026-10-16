# Experiment grid

The 30 JSON configurations are a 6-model × 5-seed reproducibility grid (seeds 11, 23, 42, 67 and 101). scripts/run_grid.py writes validation-only comparisons. Freeze the final model before holdout evaluation; seed sweeps are sensitivity analyses rather than 30 independent datasets.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
