# Baseline And Ablation

Dummy baselines estimate class priors and majority class from training only. Feature ablation trains six fresh pipelines after omitting one predictor at a time and scores validation. These are descriptive development comparisons, not causal explanations. Freeze all choices before viewing final holdout results.
