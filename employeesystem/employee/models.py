from enum import Enum
from django.db import models
from users.models import CustomUser


class Department(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)


class Employee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, unique=True)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    address = models.CharField(max_length=512)
    date_of_joining = models.DateField()


class Attendance(models.Model):
    class Status(Enum):
        PRESENT = 'present'
        ABSENT = 'absent'
        LATE = 'late'

        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]

    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    date = models.DateField()
    status = models.CharField(choices=Status.choices, max_length=8, db_index=True)


class Performance(models.Model):
    class RatingChoices(models.IntegerChoices):
        BAD = 1, 'bad'
        BELOW_AVERAGE = 2, 'below_average'
        AVERAGE = 3, 'average'
        ABOVE_AVERAGE = 4, 'above_average'
        GOOD = 5, 'good'

    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    rating = models.IntegerField(choices=RatingChoices.choices)
    review_date = models.DateField()
