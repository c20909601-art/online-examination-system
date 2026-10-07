from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    total_marks = models.IntegerField(default=100)
    pass_marks = models.IntegerField(default=40)

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    
    # Store 'option1', 'option2', 'option3', or 'option4' as the correct answer
    CORRECT_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    correct_option = models.CharField(max_length=10, choices=CORRECT_CHOICES)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question_text

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam.title} ({self.score})"