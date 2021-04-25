To install:
```bash
apt update
apt install -y git make
git clone https://github.com/senaranya/SmartCamBuddy.git
cd SmartCamBuddy
make install-prod

# From IDLE, use this to initialize DB:
>> from smarcambuddy.api import db
>> db.create_all()
```
To Upgrade:
```bash
cd SmartCamBuddy
git pull
make install-prod
```

References:
Gphoto2 API docs: http://www.gphoto.org/doc/api
Gphoto2 manual: http://www.gphoto.org/doc/manual
Gphoto2 CLI: http://www.gphoto.org/doc/manual/ref-gphoto2-cli.html
Gphoto2 Pypi: https://pypi.org/project/gphoto2

GPIO Zero: https://gpiozero.readthedocs.io/en/stable/recipes.html
Pin-out:
    https://pinout.xyz/pinout/io_pi_zero
    To see pin-out on board: command "gpio" (http://wiringpi.com/) or pinout (from gpiozero)
    How GPIO Zero library uses pins: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
Gphoto examples: /home/vagrant/.smartcambuddy_venv/share/python-gphoto2/examples/