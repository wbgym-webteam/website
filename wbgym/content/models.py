from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    year = models.PositiveSmallIntegerField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    # short hand like "herm" for "hermann" (last name)
    short = models.CharField(max_length=10)


class Article(models.Model):
    # TODO: Make it more complex, add aditional fields; maybe store even html files?
    text = models.TextField()
