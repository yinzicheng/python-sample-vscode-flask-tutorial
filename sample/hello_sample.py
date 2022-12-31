import sys
import argparse

print ('Executing script file is:', str(sys.argv[0]))
print ('The arguments are:', str(sys.argv))

parser = argparse.ArgumentParser()
parser.add_argument("--world", help="Provide the name of the world to greet.")
args = parser.parse_args()
print ('Hello ', args.world)