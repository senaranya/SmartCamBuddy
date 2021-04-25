from capture_image import CaptureImage

if __name__ == '__main__':
    """
    This can be directly used from CLI
    e.g.: source /home/pi/.smartcambuddy_venv/bin/activate
    python smarcambuddy/take_a_photo.py 
    """
    CaptureImage.trigger()
