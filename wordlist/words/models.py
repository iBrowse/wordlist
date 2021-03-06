
from django.db import models

class Word(models.Model):
    """
    Model for a word.
    'phonetic' contains a list of integers to be used with IPA_table
    'language' uses 2-letter code
    """
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255)
    phonetic = models.CharField(max_length=255)
    part_of_speech = models.CharField(max_length=64)
    language = models.CharField(max_length=16)
    definition = models.CharField(max_length=255)
    attribution = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)

    class Meta:
        db_table = "word"
