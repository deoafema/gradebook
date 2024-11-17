# Register your models here.
from django.contrib import admin
from .models import Lecturer, Student, Subject, Grade

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)
