from django.urls import path
from app.views import Home, StudentsView, StudentDetailView

urlpatterns = [
    path('', Home.as_view()),

    path('students', StudentsView.as_view()),
    path('students/<int:id>', StudentDetailView.as_view()),
]