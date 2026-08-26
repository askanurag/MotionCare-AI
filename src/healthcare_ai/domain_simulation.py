import numpy as np
import pandas as pd
def make_recording(seed=1):
    rng=np.random.default_rng(seed);t=np.arange(576)/12;state=((t//6).astype(int)%3==1).astype(int)
    glucose=95+30*state+8*np.sin(2*np.pi*t/24)+rng.normal(0,4,len(t))
    for meal in [8,13,19,32,37,43]:glucose+=20*np.exp(-.5*((t-meal)/.6)**2)
    return pd.DataFrame({'patient_id':'GLU-SIM-%03d'%seed,'hours':t,'glucose_reading':glucose,'activity':np.maximum(0,40-15*state+rng.normal(0,8,len(t))),
      'age':int(rng.integers(25,70)),'bmi':float(rng.uniform(20,35)),'family_history':int(rng.integers(0,2)),'sleep_hours':float(rng.uniform(5,9)),'latent_state':state})
