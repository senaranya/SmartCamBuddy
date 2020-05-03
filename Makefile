init:
	pip install -r requirements_dev.txt

test:
	python -m pytest tests/

lint:
	pylint **/*.py

install-prod:
	sudo apt update
	sudo apt install -y python3.7 python3.7-dev python3-pip
	sudo python3.7 -m pip install -r requirements.txt
	sudo python3.7 -m pip install ansible
	sudo ansible-playbook -i Build/inventory.ini Build/deploy-prod.yml

.PHONY: init test install
