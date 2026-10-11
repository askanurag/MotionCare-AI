"""Chunked prediction preserving original row order and identifiers."""
import pandas as pd
from .inference import predict
def predict_batches(bundle,frame,batch_size=64):
    if not isinstance(batch_size,int) or batch_size<1:raise ValueError('Positive integer batch size required')
    if len(frame)==0:return pd.DataFrame(columns=['patient_id','probability','predicted_class'])
    return pd.concat([predict(bundle,frame.iloc[i:i+batch_size]) for i in range(0,len(frame),batch_size)],ignore_index=True)
