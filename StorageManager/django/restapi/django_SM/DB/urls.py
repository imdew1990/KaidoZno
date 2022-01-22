from django.urls import path, re_path
from .views import *

app_name = 'DB'

urlpatterns = [
    re_path(r'^entrants/', EntrantsView.as_view()),
    re_path(r'^university/', UniversityView.as_view()),
    re_path(r'^faculty/', FacultyView.as_view()),
    re_path(r'^speciality/', SpecialityView.as_view()),
]