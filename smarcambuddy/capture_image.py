#!/usr/bin/env python3
"""This script ... """
from __future__ import print_function

import logging
import os
import datetime

import gphoto2 as gp


class CaptureImage:
    """This class does ... """

    @staticmethod
    def trigger():
        """This function does ... """
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(name)s: %(message)s', level=logging.INFO)
        # callback_obj = gp.check_result(gp.use_python_logging())

        camera = gp.Camera()
        camera.init()
        logging.info('Capturing image')
        start_time = datetime.datetime.now()
        file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
        logging.info('Finished copying image. Time taken: %s', str(
            (datetime.datetime.now() - start_time).total_seconds()) + ' Seconds')
        logging.info('Camera file path: %s/%s', file_path.folder, file_path.name)
        target = os.path.join('/tmp', file_path.name)
        logging.info('Copying image to %s', target)
        camera_file = camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
        camera_file.save(target)
        camera.exit()

        return 0
