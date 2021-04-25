#!/usr/bin/env python3
"""
This script ...
"""
from __future__ import print_function
import logging
import os
import datetime
import gphoto2 as gp


class CaptureImage:
    """This class does ... """

    def __init__(self, should_copy_to_sd_card = True):
        self.camera = CaptureImage.initialize_camera()
        logging.debug('Initialized camera')
        self.storage_path_on_sd_card = '/tmp'
        self.should_copy_to_sd_card = should_copy_to_sd_card

    def __del__(self):
        self.camera.exit()
        logging.debug('Closed connection to camera')

    def trigger(self):
        """
        This function captures image, and copies to SD card
        """
        file_path = CaptureImage.capture()

        if self.should_copy_to_sd_card:
            CaptureImage.copy_to_primary_sd_card(file_path)

    def initialize_camera(self):
        camera = gp.Camera()
        camera.init()
        return camera

    def capture(self):
        logging.info('Capturing image')
        start_time = datetime.datetime.now()
        file_path = self.camera.capture(gp.GP_CAPTURE_IMAGE)
        logging.info('Finished capturing image. Time taken: %s', str(
            (datetime.datetime.now() - start_time).total_seconds()) + ' Seconds')
        logging.info('Captured image on Camera: %s/%s', file_path.folder, file_path.name)
        return file_path

    def copy_to_primary_sd_card(self, file_path):
        camera_file = self.camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
        target_file = os.path.join(self.storage_path_on_sd_card, file_path.name)
        camera_file.save(target_file)
        logging.info('Copied image to %s', target_file)
