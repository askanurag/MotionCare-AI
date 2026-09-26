import numpy as np
def simulate_motion(seconds=10,fs=50,abrupt=False,seed=42):
    rng=np.random.default_rng(seed);t=np.arange(int(seconds*fs))/fs
    x=np.column_stack([np.sin(2*np.pi*1.4*t),.5*np.cos(2*np.pi*1.4*t),np.ones(len(t))])+.05*rng.normal(size=(len(t),3))
    if abrupt:x+=3*np.exp(-.5*((t[:,None]-seconds/2)/.08)**2)
    return t,x
def extract_features(x,fs=50):
    magnitude=np.linalg.norm(x,axis=1);jerk=np.diff(x,axis=0)*fs
    power=abs(np.fft.rfft(magnitude-magnitude.mean()))**2;freq=np.fft.rfftfreq(len(magnitude),1/fs)
    return {'accel_rms':float(np.sqrt(np.mean(magnitude**2))),'accel_variance':float(magnitude.var()),
       'jerk_rms':float(np.sqrt(np.mean(jerk**2))),'dominant_frequency':float(freq[np.argmax(power)])}
