
import os
import csv

from diagnosis_codes.models import Category
from mpharma_challenge.settings.base import BASE_DIR

from scripts.util import logger

VERSION='ICD-10-2018'

categories_file = os.path.join(BASE_DIR, "diagnosis_codes/data/categories.csv")

try:
    with open(categories_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:  
            try:
                Category.objects.create(version=VERSION, code=row[0], title=row[1])
                if count == 100: break 
                else: count+=1
                logger.debug("added {}, {} to categoies".format(row[0], row[1]))
            except Exception:
                logger.exception("some exception")
except Exception as e:
    logger.exception(e)
    logger.debug("Error occured in populating categories", exc_info=True)