import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file", help="beta")

args = parser.parse_args()
if Path(args.file).exists() == False:
	Path(args.file).touch()
