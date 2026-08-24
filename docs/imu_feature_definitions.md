# Imu Feature Definitions

Acceleration RMS is sqrt(mean(sum(a²))); acceleration variance is the variance of its magnitude; jerk RMS is sqrt(mean(sum((diff(a)*fs)²))); gyro RMS uses the same vector norm. Dominant frequency uses a Hann-windowed, mean-centered acceleration magnitude spectrum. Orientation change is the angle between first-quarter and last-quarter average acceleration vectors. Units are arbitrary simulator units; the angle is radians.
