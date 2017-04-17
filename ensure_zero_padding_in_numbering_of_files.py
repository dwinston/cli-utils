#!/usr/bin/env python3

import argparse
import os
import re
import sys


def main():

    parser = argparse.ArgumentParser(
        description='Ensure zero padding in numbering of files.')
    parser.add_argument(
        'path',
        type=str,
        help='path to the directory containing the files')
    args = parser.parse_args()
    path = args.path

    numbered = re.compile(r'(.*?)(\d+)\.(.*)')

    numbered_fnames = [fname for fname in os.listdir(path)
                       if numbered.search(fname)]

    max_digits = None
    for fname in numbered_fnames:
        _, prefix, num, ext, _ = numbered.split(fname, maxsplit=1)
        if max_digits is None:
            max_digits = max(len(numbered.search(fname).group(2))
                             for fname in numbered_fnames)
        num = num.zfill(max_digits)
        new_fname = "{}{}.{}".format(prefix, num, ext)
        if fname != new_fname:
            os.rename(
                os.path.join(path, fname),
                os.path.join(path, new_fname))
            print("Renamed {} to {}".format(fname, new_fname))
        else:
            print("{} seems fine".format(fname))

if __name__ == "__main__":
    sys.exit(main())
