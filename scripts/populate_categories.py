
import os
import csv
import logging


from diagnosis_codes.models import Category
from mpharmaChallenge.settings.base import BASE_DIR

logger = logging.Logger(__name__)
logger.setLevel(logging.INFO)


VERSION='ICD-10-2018'

categories_file = os.path.join(BASE_DIR,
                               "diagnosis_codes/data/categories.csv")

with open(categories_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        print(row[0], row[1])
        Category.objects.create(version=VERSION, code=row[0], title=row[1])
        if count == 100: break 
        else: count+=1