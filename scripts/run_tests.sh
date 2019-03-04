#!/bin/bash

docker exec -i ${1} coverage run --source='diagnosis_codes/' manage.py test
docker exec -i ${1} coverage report -m