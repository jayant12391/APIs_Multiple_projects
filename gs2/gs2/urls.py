

from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('studentapi/', views.StudentList.as_view()),
    path('admin/', admin.site.urls),
]



