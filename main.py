import json
import argparse

from image_utils import *

def main(cfg):
    clock, hour, minute, frs = load_assets(**cfg['loading_config'])
    gen_cfg = cfg['generation_config']

    current_time = gen_cfg['starting_time']
    delta = gen_cfg['minute_delta']
    new_frames = []
    fdelta = len(frs)//2

    for i,fr in enumerate(frs):
        rot_h = rotate_image(hour, gen_cfg['hour_med'], angle_hour(current_time[0], current_time[1]))
        rot_m = rotate_image(minute, gen_cfg['minute_med'], angle_min(current_time[1]))

        merged = merge_alpha(clock, gen_cfg['clock_med'], rot_h, gen_cfg['hour_med'])
        merged = merge_alpha(merged, gen_cfg['clock_med'], rot_m, gen_cfg['minute_med'])
        merged[merged != 0] = 255

        new_frame = merge_images(fr, frs[(i + fdelta) % len(frs)], merged, gen_cfg['clock_med'])
        cv2.imwrite(os.path.join(cfg['output_dir'], f"{i}.png"), new_frame)

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