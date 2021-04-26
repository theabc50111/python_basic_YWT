import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument("echo2")
args = parser.parse_args()
print(args.echo)
print(args.echo2)
print("finished")