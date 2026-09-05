# Architecture

CSV records pass through schema validation, patient partitioning, a training-only imputer and scaler, classifier fitting, validation threshold selection and a frozen holdout evaluation. `experiment.run` composes these modules. `cli` exposes train and predict commands.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
