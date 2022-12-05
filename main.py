import argparse
from shapes.animals import StaticTurtle


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--turtle", action="store_true", help="Draw a turtle")

args = parser.parse_args()
config = vars(args)

if config.get("turtle"):
    StaticTurtle().execute()
