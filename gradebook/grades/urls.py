from django.urls import path
from . import views

urlpatterns = [
    path('subject/<int:subject_id>/', views.subject_report, name='subject_report'),
    path('score/<int:subject_id>/<int:student_id>/', views.student_final_score, name='student_final_score'),
]
