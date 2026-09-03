# Domain Units

Domain window_size and stride_size are measured in hours. The shared API uses explicit unit metadata in every scenario. CardioWave uses seconds; GlucoRisk uses hours; CareReturn uses days for the outcome horizon, while its stride is an encounter-row selection interval. No real-device calibration or reference ranges are claimed.
