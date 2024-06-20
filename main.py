import json
import argparse

from image_utils import *

def main(cfg):
    print(cfg)
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Clock intro maker')

    parser.add_argument('-c', '--config', required=True,
                        help="Config filepath")

    args = vars(parser.parse_args())

    try:
        with open(args['config'], 'r', encoding='utf-8') as fd:
            cfg = json.load(fd)
    except IOError as err:
        print(f"Error trying to open {args['config']}. Check if file exists.")

    main(cfg)