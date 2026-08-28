import pandas as pd
from .domain_contract import validate_recording
def load_recording(path):
    frame=pd.read_csv(path);validate_recording(frame);return frame
