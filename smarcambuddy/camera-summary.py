#!/usr/bin/env python

from __future__ import print_function

import logging
import sys

import gphoto2 as gp


def main():
    logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    callback_obj = gp.check_result(gp.use_python_logging())
    camera = gp.Camera()
    camera.init()
    text = camera.get_summary()
    print('Summary')
    print('=======')
    print(str(text))
    camera.exit()
    return 0


if __name__ == "__main__":
    sys.exit(main())