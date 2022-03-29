from django.db import models


# FROM dictionary.sql
# `word` varchar(25) NOT NULL, - word
# `wordtype` varchar(20) NOT NULL, - part of speech
# 'definition` text NOT NULL - word definition

class Word(models.Model):
    word = models.CharField(max_length=30)
    wordtype = models.CharField(max_length=30)
    definition = models.CharField(max_length=255)

    def __str__(self):
        return self.word
