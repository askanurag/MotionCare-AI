from .domain_contract import validate_recording
def recording_quality(frame):
    samples_per_hour=validate_recording(frame)
    return {'samples':len(frame),'samples_per_hour':samples_per_hour,'duration_hours':len(frame)/samples_per_hour,
      'mean_reading':float(frame.glucose_reading.mean()),'reading_std':float(frame.glucose_reading.std()),'negative_readings':int((frame.glucose_reading<0).sum())}
