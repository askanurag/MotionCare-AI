# Window Overlap

All windows from a patient remain in the same partition, including overlapping windows and repeated recordings using the same identity. Window-level metric rows are dependent. The simple row-bootstrap in the original notebooks is valid only for their one-row-per-patient Gaussian dataset; do not apply it to overlapping signal windows. External patient and device evaluation are still needed.
