class Exposure:
    @classmethod
    def get_current_exposure(cls):
        # Get exposure using gphoto2
        aperture = ''
        shutter_speed = ''
        iso = ''
        return [aperture, shutter_speed, iso]

    @classmethod
    def set_current_exposure(cls, aperture, shutter_speed, iso):
        # Set exposure using gphoto2
        return
