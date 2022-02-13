from rest_framework import serializers
from .models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class QuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quota
        fields = ('id', 'quota')


class CoefficientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coefficient
        fields = '__all__'


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class EntrantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrants
        fields = '__all__'


class QuotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotas
        fields = '__all__'


class CoefficientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coefficients
        fields = '__all__'


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'


class SubjectPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectPoints
        fields = '__all__'
