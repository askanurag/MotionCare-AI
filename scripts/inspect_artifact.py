import argparse,json
from healthcare_ai.persistence import load_bundle
p=argparse.ArgumentParser(description='Inspect a TRUSTED local model artifact only');p.add_argument('bundle');args=p.parse_args();bundle=load_bundle(args.bundle)
print(json.dumps({'threshold':bundle['threshold'],'metadata':bundle['metadata']},indent=2))
