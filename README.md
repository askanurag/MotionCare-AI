# MotionCare AI

**Synthetic wearable movement classification — runnable Python research project with 30 executed Jupyter notebooks.**

Extract inertial-signal features and compare classifiers for simulated smooth versus abrupt movement. This is not a clinically validated fall detector.

## What is implemented

- Six scikit-learn baselines, 30 reproducible model/seed experiment configurations.
- Patient-level train/validation/test separation with explicit overlap checks.
- Training-only imputation and scaling; validation-only threshold selection.
- AUROC, average precision, calibration, bootstrap uncertainty, subgroup audits, permutation importance and missingness stress tests.
- Domain-specific Python utilities, CSV inference, model persistence, command-line training and Docker setup.
- 24 functional unittest modules; synthetic dataset and generated baseline reports.

## Installation

Use **Python 3.10–3.12** and a separate environment for each project. All four projects deliberately expose the same `healthcare_ai` package name; do not install them into one environment.

```bash
cd MotionCare_AI
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell instead: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[notebooks]"
```

An internet connection is needed for dependency installation. The demo does not download any dataset.

## Run end to end

```bash
python -m unittest discover -s tests -v
python -m healthcare_ai.cli train --csv data/demo.csv --output outputs/demo
python -m healthcare_ai.cli predict --bundle outputs/demo/model.joblib --csv data/examples.csv --output outputs/predictions.csv
jupyter lab notebooks
```

Training produces `outputs/demo/model.joblib` and `outputs/demo/metrics.json`. Inference writes patient IDs, class-1 probabilities and thresholded classes. Only load trusted model files.

## Experiments

```bash
python -m healthcare_ai.cli train --csv data/demo.csv --config configs/logistic_seed42.json --output outputs/logistic42
python scripts/run_grid.py
python scripts/execute_notebooks.py
python scripts/plot_report.py
```

The grid compares **validation** scores. Use training CV and validation for selection; keep test data frozen. The bundled final demo fixes logistic regression in advance. Never choose a final model by maximizing its test score.

## Data and interpretation

`data/demo.csv` contains 600 synthetic records. Inputs: accel_rms, accel_variance, jerk_rms, dominant_frequency, gyro_rms, orientation_change. Target: `simulated_movement_class`. The full mathematical generator and feature weights are in `data/schema.json` and `synthetic.py`.

All measurements and labels are simulations, not clinical observations. Simulated values can be physiologically implausible. Class-1 probabilities describe the simulated endpoint, not a medically established diagnosis. **This is an educational research prototype and has not been clinically validated.** No patient dataset or externally pretrained clinical model is included. Training commands create a fitted demo model locally.

## Repository map

| Location | Files | Purpose |
|---|---:|---|
| Root | 12 | Setup, README, license, Docker and contribution files |
| src/healthcare_ai | 30 | Reusable Python implementation |
| notebooks | 30 | Executed, topic-specific analyses |
| tests | 24 | Functional Python test modules |
| configs | 30 | Six algorithms × five random seeds |
| docs | 20 | Methods, limitations and adaptation guidance |
| scripts | 10 | Runnable workflow utilities |
| data | 16 | Synthetic records and schema |
| reports | 6 | Recomputed baseline evidence |
| .github | 2 | CI and pull-request template |
| **Total** | **180** | **64 Python files + 30 notebooks per project** |

Read `docs/file_guide.md`, `reports/model_card.md` and `reports/audit.json` before extending the project. Notebooks contain captured outputs from sequential Python cell execution; `scripts/execute_notebooks.py` supports re-execution through a Jupyter kernel. Notebook 19's domain utilities are illustrative and are not the source of the tabular simulator's training features.
