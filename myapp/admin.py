from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exam, Question, Result

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question)
admin.site.register(Result)