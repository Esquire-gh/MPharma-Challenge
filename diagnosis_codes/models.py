from django.db import models
from django.conf import settings

import os
import csv

CATEGORIES_LIST = [] 

categories_file = os.path.join(settings.BASE_DIR, "diagnosis_codes/data/categories.csv")

with open(categories_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        CATEGORIES_LIST.append((row[0], row[1]))


class DiagnosisCode(models.Model):
    category_code = models.CharField(max_length=20, choices=tuple(CATEGORIES_LIST))
    diagnosis_code = models.IntegerField(blank=True)
    full_code = models.CharField(max_length=20)
    abbreviated_description = models.CharField(max_length=300)
    full_description = models.TextField(blank=True)
    category_title = models.CharField(max_length=300)

    def __str__(self):
        return "{}, {}".format(self.category_code, self.category_title)

    