def plot_recording(frame):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(10,3));ax.plot(frame.hours,frame.glucose_reading)
    ax.fill_between(frame.hours,0,1,where=frame.latent_state.astype(bool),transform=ax.get_xaxis_transform(),alpha=.15,color='orange')
    ax.set(xlabel='Time (hours)',ylabel='Simulated glucose units',title='Synthetic glucose trace; shaded injected elevated states')
    fig.tight_layout();return fig
