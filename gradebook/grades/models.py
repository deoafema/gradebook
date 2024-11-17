# Create your models here.
from django.db import models

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    def compute_final_score(self, subject):
        # Fetch all grades for this student and the specific subject
        grades = Grade.objects.filter(student=self, subject=subject)

        # Define the weights for each grade type
        weights = {
            'assignment': 0.3,
            'quiz': 0.2,
            'exam': 0.5,
        }

        # Initialize total score and weight accumulator
        total_score = 0
        total_weight = 0

        # Calculate the weighted average
        for grade in grades:
            weight = weights.get(grade.grade_type, 0)
            total_score += grade.score * weight
            total_weight += weight

        # If no grades, return 0
        if total_weight == 0:
            return 0

        return round(total_score / total_weight, 2)  # Final score out of 100

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):
    GRADE_CHOICES = [
        ('assignment', 'Assignment'),
        ('quiz', 'Quiz'),
        ('exam', 'Exam'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_type = models.CharField(max_length=10, choices=GRADE_CHOICES)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.grade_type})"
