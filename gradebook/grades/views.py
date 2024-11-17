# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Subject, Grade, Student

def subject_report(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    grades = Grade.objects.filter(subject=subject)

    scores = [grade.score for grade in grades]
    if scores:
        average_score = sum(scores) / len(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
    else:
        average_score = highest_score = lowest_score = None

    context = {
        'subject': subject,
        'average_score': average_score,
        'highest_score': highest_score,
        'lowest_score': lowest_score,
        'grades': grades,
    }
    return render(request, 'grades/subject_report.html', context)

def student_final_score(request, student_id, subject_id):
    student = get_object_or_404(Student, id=student_id)
    subject = get_object_or_404(Subject, id=subject_id)

    final_score = student.compute_final_score(subject)

    return render(request, 'grades/student_final_score.html', {
        'student': student,
        'subject': subject,
        'final_score': final_score,
    })