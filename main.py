import json
import argparse

from image_utils import *

def main(cfg):
    c, h, m, frs = load_assets(**cfg['loading_config'])
    gen_cfg = cfg['generation_config']

    current_time = gen_cfg['starting_time']
    delta = gen_cfg['minute_delta']
    for fr in frs:
        print(current_time)

        if current_time[1] + delta > 60:
            add_hour = 1
        elif current_time[1] + delta < 0:
            add_hour = -1
        else:
            add_hour = 0
        current_time = [(current_time[0] + add_hour) % 12, 
                        ((current_time[1] + delta) % 60)]

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