def segment_label(segment,positive_fraction=.5):
    if len(segment)==0 or not 0<positive_fraction<=1:raise ValueError('Nonempty segment and valid fraction required')
    return int(float(segment.latent_state.mean())>=positive_fraction)
