from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class University(models.Model):
    id = models.AutoField(primary_key=True)
    university_name = models.TextField(unique=False)
    faculty_name = models.TextField(unique=False)
    speciality_name = models.TextField(unique=False)
    edu_program = models.TextField(unique=False)
    degree = models.CharField(max_length=32, unique=False)
    year = models.DateField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['university_name'])
        ]


class Quota(models.Model):
    id = models.AutoField(primary_key=True)
    quota = models.CharField(max_length=3)

    class Meta:
        indexes = [
            models.Index(fields=['quota'])
        ]


class Coefficient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2)
    count = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Points(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.DecimalField(max_digits=5, decimal_places=2)


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=128)

    class Meta:
        indexes = [
            models.Index(fields=['subject_name'])
        ]


class Entrants(models.Model):
    id = models.AutoField(primary_key=True)
    university_id = models.ForeignKey(University, on_delete=models.RESTRICT)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    point = models.DecimalField(max_digits=6, decimal_places=3)
    type = models.CharField(max_length=1)
    submited_docs = models.BooleanField(default=False)


class Quotas(models.Model):
    quota_id = models.ForeignKey(Quota, on_delete=models.RESTRICT)
    entrants_id = models.ForeignKey(Entrants, on_delete=models.RESTRICT)


class Coefficients(models.Model):
    coefficient_id = models.ForeignKey(Coefficient, on_delete=models.RESTRICT)
    entrants_id = models.ForeignKey(Entrants, on_delete=models.RESTRICT)


class Marks(models.Model):
    entrants_id = models.ForeignKey(Entrants, on_delete=models.RESTRICT)
    point_id = models.ForeignKey(Points, on_delete=models.RESTRICT)
    subject_id = models.ForeignKey(Subject, on_delete=models.RESTRICT)


class SubjectPoints(models.Model):
    university_id = models.ForeignKey(University, on_delete=models.RESTRICT)
    subject_id = models.ForeignKey(Subject, on_delete=models.RESTRICT)
    point = models.DecimalField(max_digits=2, decimal_places=2)