import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponet")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print("running '{}'".format(__file__))
elif args.verbosity >=1:
    print("{}^{} == ".format(args.x, args.y), answer, end="")
else:
    print(answer)
