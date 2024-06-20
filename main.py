import json
import argparse

from image_utils import *

def main(cfg):
    c, h, m, frs = load_assets(**cfg['loading_config'])
    gen_cfg = cfg['generation_config']

    starting_hour = gen_cfg['starting_hour']
    for fr in frs:
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