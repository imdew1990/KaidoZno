from django.urls import path, re_path
from .views import *

app_name = 'DB'

urlpatterns = [
    re_path(r'^quota/', QuotaView.as_view()),
    re_path(r'^coefficient/', CoefficientView.as_view()),
    re_path(r'^points/', PointsView.as_view()),
    re_path(r'^subject/', SubjectView.as_view()),
    re_path(r'^quotas/', QuotasView.as_view()),
    re_path(r'^coefficients/', CoefficientsView.as_view()),
    re_path(r'^marks/', MarksView.as_view()),
    re_path(r'^entrants/', EntrantsView.as_view()),
    re_path(r'^subjectpoints/', SubjectPointsView.as_view()),
    re_path(r'^university/', UniversityView.as_view()),
]