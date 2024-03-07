import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--narg_number", nargs=3)          # 能接收3個arg
parser.add_argument("--narg_plus", nargs="+")          # 能接收1~n個arg
parser.add_argument("--narg_question", nargs="?")      # 只能接收0~1個arg
parser.add_argument("--narg_asterisk", nargs="*")      # 能接收0~n個arg
args = parser.parse_args()
print(f"args.narg_number: {args.narg_number}, type(args.narg_number): {type(args.narg_number)}")
print(f"args.narg_plus: {args.narg_plus}, type(args.narg_plus): {type(args.narg_plus)}")
print(f"args.narg_question: {args.narg_question}, type(args.narg_question): {type(args.narg_question)}")
print(f"args.narg_asterisk: {args.narg_asterisk}, type(args.narg_asterisk): {type(args.narg_asterisk)}")
print("argarse_nargs.py finished")