from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class EntrantsView(APIView):
    def get(self, request):
        entrants = Entrants.objects.all()
        if entrants:
            entrants_serializer = EntrantsSerializer(entrants, many=True)
            result = entrants_serializer.data
            return JsonResponse(result, safe=False)
        return JsonResponse('Table Entrants is empty.', safe=False)

    def post(self, request):
        entrants_data = JSONParser().parse(request)
        entrants_serializer = EntrantsSerializer(data=entrants_data)
        if entrants_serializer.is_valid():
            entrants_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)

    def put(self, request):
        entrant_data = JSONParser().parse(request)
        if entrant_data.get('id', -1) != -1:
            entrant = Entrants.objects.get(id=entrant_data['id'])
            for key in entrant_data:
                setattr(entrant, key, entrant_data[key])
                print(getattr(entrant, key), sep=' ', end=' ')
            entrant.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    def delete(self, request):
        request_data = JSONParser().parse(request)
        id = request_data['id']
        entrant = Entrants.objects.get(id=id)
        entrant.delete()
        return JsonResponse('Deleted Successfully', safe=False)


class UniversityView(APIView):
    def get(self, request):
        universities = University.objects.all()
        if universities:
            university_serializer = UniversitySerializer(universities, many=True)
            result = university_serializer.data
            return JsonResponse(result, safe=False)
        return JsonResponse('Table University is empty.', safe=False)

    def post(self, request):
        universities_data = JSONParser().parse(request)
        universities_serializer = UniversitySerializer(data=universities_data)
        if universities_serializer.is_valid():
            universities_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)

    def put(self, request):
        universities_data = JSONParser().parse(request)
        if universities_data.get('id', -1) != -1:
            university = University.objects.get(id=universities_data['id'])
            for key in universities_data:
                setattr(university, key, universities_data[key])
                print(getattr(university, key), sep=' ', end=' ')
            university.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    def delete(self, request):
        request_data = JSONParser().parse(request)
        id = request_data['id']
        university = University.objects.get(id=id)
        university.delete()
        return JsonResponse('Deleted Successfully', safe=False)


class FacultyView(APIView):
    def get(self, request):
        faculties = Faculty.objects.all()
        if faculties:
            faculties_serializer = FacultySerializer(faculties, many=True)
            result = faculties_serializer.data
            return JsonResponse(result, safe=False)
        return JsonResponse('Table University is empty.', safe=False)

    def post(self, request):
        faculty_data = JSONParser().parse(request)
        faculty_serializer = FacultySerializer(data=faculty_data)
        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)

    def put(self, request):
        faculties_data = JSONParser().parse(request)
        if faculties_data.get('id', -1) != -1:
            faculty = Faculty.objects.get(id=faculties_data['id'])
            for key in faculties_data:
                setattr(faculty, key, faculties_data[key])
                print(getattr(faculty, key), sep=' ', end=' ')
            faculty.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    def delete(self, request):
        request_data = JSONParser().parse(request)
        id = request_data['id']
        faculty = Faculty.objects.get(id=id)
        faculty.delete()
        return JsonResponse('Deleted Successfully', safe=False)


class SpecialityView(APIView):
    def get(self, request):
        specialities = Speciality.objects.all()
        if specialities:
            specialities_serializer = SpecialitySerializer(specialities, many=True)
            result = specialities_serializer.data
            return JsonResponse(result, safe=False)
        return JsonResponse('Table University is empty.', safe=False)

    def post(self, request):
        speciality_data = JSONParser().parse(request)
        speciality_serializer = SpecialitySerializer(data=speciality_data)
        if speciality_serializer.is_valid():
            speciality_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)

    def put(self, request):
        speciality_data = JSONParser().parse(request)
        if speciality_data.get('id', -1) != -1:
            faculty = Speciality.objects.get(id=speciality_data['id'])
            for key in speciality_data:
                setattr(faculty, key, speciality_data[key])
                print(getattr(faculty, key), sep=' ', end=' ')
            faculty.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    def delete(self, request):
        request_data = JSONParser().parse(request)
        id = request_data['id']
        speciality = Speciality.objects.get(id=id)
        speciality.delete()
        return JsonResponse('Deleted Successfully', safe=False)
