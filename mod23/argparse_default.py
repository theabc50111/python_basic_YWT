import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--flag_default", default="customize default")          # 能接收3個arg
args = parser.parse_args()
print(f"args.flag_default: {args.flag_default}, type(args.flag_default): {type(args.flag_default)}")
print("argarse_default.py finished")