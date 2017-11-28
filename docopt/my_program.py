#! /usr/bin/env python3
"""
Naval Fate.

Usage:
  naval_fate ship new <name>...
  naval_fate ship <name> move <x> <y> [--speed=<kn>]
  naval_fate ship shoot <x> <y>
  naval_fate mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate -h | --help
  naval_fate -v,--version

Options:
  -h --help     Show this screen.
  -v,--version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""

import docopt
opts = docopt.docopt(__doc__, version='0.0.1')

for k, v in opts.items():
    print('\t', k, v)

