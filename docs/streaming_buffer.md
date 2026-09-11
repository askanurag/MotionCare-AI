# Streaming Buffer

WindowBuffer accumulates finite six-axis chunks, emits copies of complete windows and retains only the unconsumed suffix. Tests compare chunked emission against offline windowing, including non-divisible chunk lengths. It does not handle packet time synchronization, clinical alerts, authentication or network transport.
