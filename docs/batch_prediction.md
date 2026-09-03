# Batch Prediction

batch_inference.predict_batches splits an inference table into bounded row batches, preserves original row order and identifiers and delegates schema checking to the existing inference module. Empty inputs return an empty result table. Only load trusted joblib artifacts; batching does not provide authentication or privacy controls.
