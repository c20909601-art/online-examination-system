from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam, Question, Result

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'myapp/exam_list.html', {'exams': exams})

@login_required
def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all()

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option == question.correct_option:
                score += question.marks

        result = Result.objects.create(
            user=request.user,
            exam=exam,
            score=score,
            total_questions=total_questions
        )
        return redirect('exam_result', result_id=result.id)

    return render(request, 'myapp/take_exam.html', {'exam': exam, 'questions': questions})

@login_required
def exam_result(request, result_id):
    result = get_object_or_404(Result, id=result_id, user=request.user)
    return render(request, 'myapp/result.html', {'result': result})
from django.shortcuts import render, redirect
from .forms import ExamForm

def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'myapp/create_exam.html', {'form': form})