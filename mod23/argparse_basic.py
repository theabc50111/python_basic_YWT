import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--flag1")
parser.add_argument("--flag2")
args = parser.parse_args()
print(f"result of args.flag1: {args.flag1}, type(args.flag1): {type(args.flag1)}")
print(f"result of args.flag2: {args.flag2}, type(args.flag1): {type(args.flag2)}")
print("argparse_basic.py finished")