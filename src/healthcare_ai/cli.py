import argparse
import json
from .synthetic import generate
from .io import load_csv
from .experiment import run
from .inference import predict
from .persistence import load_bundle
from .config import read_config
def main():
    parser=argparse.ArgumentParser(description='Synthetic healthcare ML research toolkit')
    sub=parser.add_subparsers(dest='command',required=True)
    train=sub.add_parser('train');train.add_argument('--csv');train.add_argument('--model',default='logistic');train.add_argument('--seed',type=int,default=42);train.add_argument('--config');train.add_argument('--output',default='outputs/demo')
    infer=sub.add_parser('predict');infer.add_argument('--bundle',required=True);infer.add_argument('--csv',required=True);infer.add_argument('--output',default='predictions.csv')
    args=parser.parse_args()
    if args.command=='train':
        cfg=read_config(args.config) if args.config else {'model':args.model,'seed':args.seed}
        _,report=run(load_csv(args.csv) if args.csv else generate(seed=cfg['seed']),cfg['model'],cfg['seed'],args.output)
        print(json.dumps(report,indent=2))
    else: predict(load_bundle(args.bundle),load_csv(args.csv,False)).to_csv(args.output,index=False)
if __name__=='__main__': main()
