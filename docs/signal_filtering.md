# Signal Filtering

The zero-phase Butterworth low-pass function uses future samples, so it is appropriate only for offline analysis. Its output is not used by the default raw-window training pipeline. The streaming buffer only batches raw windows and does not make the offline filter causal. A real-time adaptation needs causal filtering and latency validation.
