# Model artifacts

Training saves model.joblib plus metrics.json under the chosen output directory. Metadata records software versions, the input CSV hash and random seed. Joblib uses pickle semantics: only load trusted local artifacts. No clinical or externally pretrained weights are supplied.

Project context: Synthetic wearable movement classification. See `data/schema.json` for the feature contract and `README.md` for executable commands.
