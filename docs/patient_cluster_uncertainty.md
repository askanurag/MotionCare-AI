# Patient Cluster Uncertainty

Domain rows may repeat a patient. Use cluster_bootstrap.cluster_auc to resample whole patient clusters. Its percentile interval is conditional on the trained model and supplied patient sample. Very few test patients produce unstable intervals; it is not a population-level performance guarantee. The original row-bootstrap notebooks apply only to their one-row-per-patient Gaussian demo.
