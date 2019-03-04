from django.db import models
from django.conf import settings

import os
import csv

CODE_VERSION = (
    ('ICD-10-2018', 'ICD-10 Verion:2018'),
)

class Category(models.Model):
    version = models.CharField(max_length=30, choices=CODE_VERSION)
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=300)

    def __str__(self):
        return "{}, {}".format(self.code, self.title)


class DiagnosisCode(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    diagnosis_code = models.IntegerField(blank=True)
    full_code = models.CharField(max_length=20)
    abbreviated_description = models.CharField(max_length=300)
    full_description = models.TextField()

    def __str__(self):
        return "{}, {}".format(self.full_code, self.full_description)