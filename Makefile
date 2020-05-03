init:
	pip install -r requirements_dev.txt

test:
	python -m pytest tests/

lint:
	pylint **/*.py

install-prod:
	sudo apt update
	sudo apt install -y python3.8 python3.8-dev python3-pip
	sudo python3.8 -m pip install -r requirements.txt
	sudo python3.8 -m pip install ansible
	sudo ansible-playbook -i Build/inventory.ini Build/deploy-prod.yml

.PHONY: init test install
