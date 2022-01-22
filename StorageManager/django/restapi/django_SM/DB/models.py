from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    edu_program = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'edu_program'], name='UNIQUE_name_edu')
        ]
        indexes = [
            models.Index(fields=['name', 'edu_program'])
        ]


class Entrants(models.Model):
    id = models.AutoField(primary_key=True)
    university_id = models.ForeignKey(University, on_delete=models.RESTRICT)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.RESTRICT)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.RESTRICT)
    year = models.DateField(auto_now=True)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    point = models.DecimalField(max_digits=6, decimal_places=3)
    points = models.JSONField()
    coeficients = models.JSONField()
    quoats = models.JSONField()

    def update(self, **kwargs):
        pass

