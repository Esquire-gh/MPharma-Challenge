#!/bin/bash

coverage run --source='diagnosis_codes/' manage.py test
coverage report -m