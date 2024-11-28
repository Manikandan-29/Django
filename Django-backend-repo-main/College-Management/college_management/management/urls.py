from django.urls import path
from . import views
from .models import SubjectDetails
from .models import StudentDetails
urlpatterns = [
    path('users/', views.usersViewset.as_view()),             # GET all, POST new user
    path('users/<str:reg_emp_id>/', views.usersViewset.as_view()),    # GET, PATCH, DELETE a specific user
    
    path('studentdetails/', views.StudentDetailsViewset.as_view()),             # GET all, POST new student
   # path('studentdetails/<int:id>/', views.StudentDetailsViewset.as_view()),    # GET, PATCH, DELETE a specific student
    path('studentdetails/<str:reg_emp_id>/', views.StudentDetailsViewset.as_view()),  # For reg_emp_id handling
    path('subjectdetails/', views.SubjectDetailsViewset.as_view()),
    path('subjectdetails/<str:reg_emp_id>/', views.SubjectDetailsViewset.as_view()),
]