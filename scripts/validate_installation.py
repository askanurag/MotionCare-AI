import platform,sklearn,numpy,pandas,scipy
from healthcare_ai.settings import FEATURES,TARGET
print({'python':platform.python_version(),'sklearn':sklearn.__version__,'numpy':numpy.__version__,'pandas':pandas.__version__,'scipy':scipy.__version__,'features':FEATURES,'target':TARGET})
