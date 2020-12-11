import argparse
import logging

import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.append("../")
import utils

from stacker import *

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level="INFO"
)


def parse_command_line(args):
    """Parse args passed to the stacking script.

    Args:
        args (list of str): Command line arguments to parse.

    Returns:
        Namespace with members for all parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Stack images from a video or image directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--image_source",
        type=str,
        required=True,
        help="Path to image source. It could be a single video file or a directory of images.",
    )
    parser.add_argument(
        "-o",
        "--output_path",
        required=True,
        type=str,
        help="Absolute output directory where stacked image will be stored.",
    )
    parser.add_argument(
        "-s",
        "--sampling_rate",
        required=False,
        default=1,
        type=int,
        help="Sampling rate. 1 means every frame will be used, 10 means every 10th frame will be used.",
    )
    parser.add_argument(
        "-start",
        "--start_idx",
        required=False,
        default=0,
        type=int,
        help="Start index.",
    )
    parser.add_argument(
        "-end",
        "--end_idx",
        required=False,
        default=-1,
        type=int,
        help="End index.",
    )
    return parser.parse_args(args)


def main(args=None):
    """Stack images."""
    args = parse_command_line(args)
    
    # Extract images from video
    # TODO generalize for video vs img_dir

    # utils.extract_images_from_video(args.image_source, args.output_path)
    stacker = Stacker(args.output_path,
                      sampling_rate=args.sampling_rate,
                      start_idx=args.start_idx,
                      end_idx=args.end_idx)
    mean_img = stacker.stack()
    cv2.imwrite(args.output_path + "/stacked_img.jpg", mean_img)

if __name__ == "__main__":
    main()
