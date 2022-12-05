import argparse
from shapes.animals import StaticTurtle
from shapes.flags import UkraineFlag

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-turtle", "--turtle", action="store_true", help="Draw a turtle")
parser.add_argument("-ukr", "--ukraine", action="store_true", help="Draw Ukrainian flag")

args = parser.parse_args()
config = vars(args)


if config.get("turtle"):
    StaticTurtle().execute()

elif config.get("ukraine"):
    UkraineFlag().execute()

