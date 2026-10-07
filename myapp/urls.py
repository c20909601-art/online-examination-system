from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.take_exam, name='take_exam'),
    path('result/<int:result_id>/', views.exam_result, name='exam_result'),
    path('create-exam/', views.create_exam, name='create_exam'),
]