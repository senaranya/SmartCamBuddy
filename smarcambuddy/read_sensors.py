from capture_image import CaptureImage
from gpiozero import Button, LED, Buzzer
from signal import pause
import logging

led = LED('BCM17')
button = Button('BCM2')

def button_pressed():
    led.source = button
    CaptureImage.trigger()
    logging.info("Handled button press")

if __name__ == '__main__':
    """
    While developing, this can be used as:
        supervisorctl stop smartcambuddy
        source /home/pi/.smartcambuddy_venv/bin/activate
        python SmartCamBuddy/smarcambuddy/read_sensors.py
    """

    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(name)s: %(message)s', level=logging.INFO)

    logging.info('Started')
    button.when_pressed = button_pressed

    pause()
    logging.info('Finished')
