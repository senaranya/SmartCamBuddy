import sys
import pytest
from capture_image import CaptureImage

def test_trigger_function_triggers_a_photo():
    photoPath = CaptureImage.trigger()
    # assert photoPath exists
    # assert photoPath contains a valid photo
    # delete photoPath


def fizzBuzz(value):
    return str(value)


def test_returns1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == "1"


def test_returns2With2PassedIn():
    retVal = fizzBuzz(2)
    assert retVal == "2"
