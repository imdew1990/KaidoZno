from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class View(APIView):
    def __init__(self):
        self.table = None
        self.serializer = None

    def _get_data(self, id=None):
        if id is None:
            return self.table.objects.all()
        return self.table.objects.get(id=id)

    def _get_serializer(self, data, many):
        return self.serializer(data=data, many=many)

    def get(self, request):
        """Get all data from table"""
        data = self._get_data()
        if data:
            serializer = self._get_serializer(data, many=True)
            if serializer.is_valid():
                pass
            result = serializer.data
            return JsonResponse(result, safe=False)
        return JsonResponse('Table is empty.', safe=False)

    def post(self, request):
        """Insert data to table"""
        data = JSONParser().parse(request)
        serializer = self._get_serializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)

    def put(self, request):
        """Update data from table"""
        data = JSONParser().parse(request)
        if data.get('id', -1) != -1:
            inserted_data = self._get_data(id=data['id'])
            for key in data:
                setattr(inserted_data, key, data[key])
                print(getattr(inserted_data, key), sep=' ', end=' ')
            inserted_data.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    def delete(self, request):
        """Delete data from table"""
        request_data = JSONParser().parse(request)
        id = request_data['id']
        object = self._get_data(id=id)
        if object:
            object.delete()
            return JsonResponse('Deleted Successfully', safe=False)
        return JsonResponse('Failed to delete', safe=False)

class QuotaView(View):
    def __init__(self):
        self.table = Quota
        self.serializer = QuotaSerializer


class CoefficientView(View):
    def __init__(self):
        self.table = Coefficient
        self.serializer = CoefficientSerializer


class PointsView(View):
    def __init__(self):
        self.table = Points
        self.serializer = PointsSerializer


class SubjectView(View):
    def __init__(self):
        self.table = Subject
        self.serializer = SubjectSerializer


class QuotasView(View):
    def __init__(self):
        self.table = Quotas
        self.serializer = QuotasSerializer


class CoefficientsView(View):
    def __init__(self):
        self.table = Coefficients
        self.serializer = CoefficientsSerializer


class MarksView(View):
    def __init__(self):
        self.table = Marks
        self.serializer = MarksSerializer


class SubjectPointsView(View):
    def __init__(self):
        self.table = SubjectPoints
        self.serializer = SubjectPointsSerializer


class EntrantsView(View):
    def __init__(self):
        self.table = Entrants
        self.serializer = EntrantsSerializer


class UniversityView(View):
    def __init__(self):
        self.table = University
        self.serializer = UniversitySerializer
