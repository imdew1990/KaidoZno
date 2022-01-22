from rest_framework import serializers
from .models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'name')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name')


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'name', 'edu_program')


class EntrantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrants
        fields = ('id', 'university_id', 'faculty_id', 'speciality_id', 'year', 'priority', 'point', 'points',
                  'coeficients', 'quoats')
