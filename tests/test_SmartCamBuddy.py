import smarcambuddy
import pytest


def fizzBuzz(value):
    return str(value)

def test_returns1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == "1"
    assert False

def test_returns2With2PassedIn():
    retVal = fizzBuzz(2)
    assert retVal == "2"